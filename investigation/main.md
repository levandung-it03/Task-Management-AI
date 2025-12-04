# Our Problem
## 1. Description
Need a model to satisfy the prediction of `n` Users that meet the demand of Leader, base on:
- `task_type`
- `priority`
- `level`
- `is_on_time` (`true`/`false`)
- `free_time_perct` (`[0;1]`)
- `lt_ratio` (`[0;1]`)

## 2. Problems
### a. An empty beginning
What if `Task` input values as `type`, `level`, `priority` doesn't exist in dataset yet?
```md
dataset = [
    ['DEV', 'URGENT', 'HARD', 1, 0.33],
    ['DEV', 'HIGH', 'LIGHT', 1, 0.33],
    ['DEV', 'URGENT', 'NORMAL', 1, 0.33],
]
# priority='LOW' doesn't exist in dataset
input_task = ['DEV', 'LOW', 'HARD']
```

### b. Updatable in short-time
This is required. The workflows are:
- Employees (has been assigned to a `Task`) submitted an approved `Report`.
- Trigger `Spring Service` to send data to `FastAPI` service.
- Update dataset, and train model again.
- Right after Employee submit `Task`, Leader predict best `n` Users.
- Open `stream` to `NextJS` by `WebSocket` that:
    > Model is updating in `5-10 minutes`, and the current result may not the best.

**Note**: Determine limited-time between 2 training jobs (protect `FastAPI` server from out-of-memory problem).

### c. Work correctly in a large dataset:
Simply calculate an example:
- Got 1,000 `Users`.
- Each one submitted 100 Reports in a year (means did 100 `Tasks`).
> We got 100,000 Records of Users submitted Tasks annually.

### d. Business Logic
[?] _In `n` Users output, how many `Users` is in-progress on another `Task`?_
> Query & send `busy_users` along with `input_task`. <br>
> Filter the scored-list (sorted suitable Users-List) and then get `n` top Users.

[?] _If chosen model is serving **classification-problem**, can it cover the large number of labels, when each `user_id` is
a label?_

## 3. Choosing Model
### a. `Learning-to-Rank` problem
We **_teach_** a model to sort (**ranking**) the dataset by the requirement fields, rather than the traditional output
is _one-label_.

`Learning-to-Rank` (or `LTR`) has 3 key-parts:
- Query – input value (want to predict).
- Candidate Items – the whole data that will be sorted.
- Relevance Label – the suitable "**score**" between _Query_ and each _Candidate Item_. (if score=1, it's always chosen, and 0 is the opposite).

[?] _What if we compare it with DB Index mechanism?_

| Tiêu chí                            | DB Query + Index                                                                  | Learning-to-Rank                                                                                  |
| ----------------------------------- | --------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------- |
| **Cơ chế**                          | Dùng **filter/sort** theo điều kiện cứng (SQL `WHERE`, `ORDER BY`)                | Học một **hàm score** phức tạp từ dữ liệu (có thể phi tuyến tính)                                 |
| **Hiệu quả**                        | Rất nhanh, tối ưu bởi DB engine, nhưng chỉ sort được theo cột đơn giản            | Cũng nhanh (sau khi train) vì chỉ là tính toán score, nhưng có thể kết hợp nhiều feature phức tạp |
| **Khả năng tổng quát (generalize)** | Không có — chỉ lọc theo giá trị chính xác (exact match)                           | Có — có thể xếp hạng cho query chưa từng thấy trong dữ liệu, dựa vào pattern đã học               |
| **Trọng số**                        | Không có — phải viết thủ công (ví dụ ORDER BY free\_time DESC, is\_on\_time DESC) | Tự học trọng số (weight) của từng feature, biết feature nào quan trọng hơn                        |
| **Cập nhật**                        | Dữ liệu mới có thể dùng ngay (insert/update record)                               | Phải train/fine-tune model (mất 1-5 phút tùy dataset)                                             |
| **Độ phức tạp business logic**      | Dễ — chỉ là rule-based                                                            | Có thể encode business logic bằng feature engineering, nhưng khó debug hơn                        |

[?] _Cases that DB cannot handle?_

| user_id | domain | level        | priority   | on_time | free_time |
|---------|--------|--------------|------------|---------|-----------|
| 1       | DEV    | HARD (3)     | HIGH (2)   | 1       | 0.1       |
| 1       | DEV    | HARD (3)     | HIGH (2)   | 1       | 0.1       |
| 2       | DEV    | ADVANCED (2) | NORMAL (1) | 1       | 0.2       |
> What if request data: { domain: "DEV", level: "HARD", priority: "NORMAL"}. And the employees is 1, what's the result?

```md
LightGBM does:

---Employee 1---
domain_match = 1
level_diff = |3 - 3| = 0
priority_diff = |1 - 2| = 1
on_time = 1
free_time = 0.1

---Employee 2---
domain_match = 1
level_diff = |3 - 2| = 1
priority_diff = |1 - 1| = 0
on_time = 1
free_time = 0.2
```

[?] _How many filters we need to implement?_
```md
1. "domain" filter on scores_list.
2. busy_users = [user_1, user_2,...] filter on unique_user_list.
```

### b. About Boosting Algorithm
Gradient Boosted Decision Trees (GBDT)
> mỗi cây cố gắng sửa lỗi của tập ensemble hiện tại.

### c. `LightGBM` model from _Microsoft_
**Light Gradient Boosting Machine** which is based on _Gradient Boosting Decision Trees (GBDT)_ aggregates by
_Weak Decision Trees_. It's better that allows new features:
- Histogram-based splitting (reduce comparing expressions).
- Leaf-wise growth (faster and deeper tree building).
- Support GPU.

Main idea:
1. Start with a basic & small **Tree**.
2. Start predicting → got residual (sai số) with real labels.
3. Train next **Tree** to get the better prediction.
4. Repeat training → got “weak learners”, aggregate to a strong model.

With `Learning-to-Rank`, uses basic `LambdaRank` mechanism (most popular):
- Input:
  1. Query = assigning `Task`.
  2. Candidates = list `Users`.
  3. Label = suitable score (relevance), example:
  ```md
  1 = User's done Task, has appropriate data with assigning Task.
  0 = User's failed, or never done.
  ```
- With each `Query`, model consider users in pair (u_i, u_j):
```md
If label(u_i) > label(u_j)
=> model learn how to make score(u_i) > score(u_j).

Otherwise, model predict wrong oder
=> Generate gradient (λ) to update.
```
- Loss function = logistic loss base on **_pairwise_**, with more weights **_NDCG_** to get correct top on list.

> Result: model learnt a scoring-function f(query, user). <br>
> Calculate score for new Task assign for each `user → sort → top n`.

---
# Score of model

Độ phù hợp `Score` này khác với `score` tính performance nhé.  
Ex:
```md
user_A = Làm 100 task(level=4, priority=4,...)
user_B = Làm 10 task(level=2, priority=2,...)

Nếu tính performance score bình thường, thì user_A chắc chắn sẽ cao hơn.
> Nhưng tính bằng model, (level=2,priority=1) thì user_B sẽ score model cao hơn, và thực tế nếu cứ gán cho
A thì sẽ b hao phí nguồn lực.
```

---
# Techniques

| Applied Technique    | Details                                                                                                                                                                                                          |
|----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Aggregating Profiles | For grouping records by `user_id & domain`, and make the dataset records various (`prfm`, `consist`,...).                                                                                                        |
| Stating Profiles     | Because of `Learning-to-Rank` Problem, we need to score all **user-profiles**. <br>And always keep it on server in a map `user_id::domain`.                                                                      |
| Busy `user_ids`      | With Stating-Profiles, we can filter `user_ids` firstly.                                                                                                                                                         |
| LightGBM Booster     | Continue applying new **Boosting-Tree** by `new_df`. <br>This one keep **smallest latency** between _retraining_-_predicting_.<br>Consider to retrain-model, or using booster (**low-acc**, or **high-latency**) |

# Why not "late_time"?
Model cannot understand that high `late_time` is a bad condition, it just know how to find the threshold, that will
classify the input data onto the right branch/leaf. So that we have to change it to
> punctuality_score = 1 - late_time_perct

```md
From GPT
Bạn không tìm "user tốt nhất" mà tìm "user phù hợp nhất" với:

Level gần target nhất

Priority handling phù hợp nhất

Availability đủ tốt

→ Classification làm EXACTLY điều này!
```