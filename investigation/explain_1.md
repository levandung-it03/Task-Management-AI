
## **Giả sử bạn có:**

1. **Dataset `df` ~100k dòng** (mỗi dòng = một task đã được assign user):

| user_id | domain  | level    | priority | is_on_time | free_time_rto | late_time_perct |
| ------- | ------- | -------- | -------- | ---------- | --------------- | --------------- |
| 1       | BACKEND | ADVANCED | NORMAL   | 0.9        | 0.3             | 0.1             |
| 2       | BACKEND | ADVANCED | NORMAL   | 0.7        | 0.5             | 0.2             |

2. **Model đã train** trên toàn bộ dataset với features:

```
[domain, level, priority, is_on_time, free_time_rto, late_time_perct]
```

* Label = `user_id` (ai được assign task)

3. **Input prediction** mới (TaskUserPredRequest):

* domain, level, priority
* số lượng employee cần (`num_of_emp`)
* busy_ids (loại trừ những user đang bận)

---

## **Luồng hoạt động chi tiết**

### **Bước 1: Lấy candidate users**

* Lọc dataset để tìm tất cả user từng làm việc ở domain đó:

```python
candidate_users = df.loc[df['domain'] == request.domain, 'user_id'].unique()
```

* Nếu không có ai match domain → fallback: tất cả user

> Kết quả: danh sách user candidate, ví dụ `[1,2,3,...]`

---

### **Bước 2: Chuẩn bị input cho model**

* Model đã train với **6 features**: `domain, level, priority, is_on_time, free_time_rto, late_time_perct`
* Input prediction ban đầu chỉ có 3 field (`domain, level, priority`)
* Do đó phải điền các **feature còn lại thuộc user** từ lịch sử:

```python
user_stats = df.groupby('user_id').agg({
    'is_on_time':'mean',
    'free_time_rto':'mean',
    'late_time_perct':'mean'
})

result_candidates = pd.DataFrame([
    {
        'user_id': user,
        'domain': request.domain,
        'level': request.level,
        'priority': request.priority,
        'is_on_time': user_stats.loc[user, 'is_on_time'],
        'free_time_rto': user_stats.loc[user, 'free_time_rto'],
        'late_time_perct': user_stats.loc[user, 'late_time_perct']
    }
    for user in candidate_users
])
```

* Kết quả: DataFrame **n_user × 6 features**, sẵn sàng cho `.predict()`

---

### **Bước 3: Predict với model**

* Gọi:

```python
scores = model.predict(result_candidates.drop(columns=['user_id']))
```

* Model dùng **6 features** của từng user → dự đoán user_id / score tương ứng
* Output `scores` có **n_user giá trị**, phản ánh **mức “fit” của mỗi user với task mới**

> Lưu ý: LightGBM dự đoán label (`user_id`), nếu muốn **score ranking**, bạn có thể dùng `predict_proba` và lấy xác suất mỗi user là “best candidate”.

---

### **Bước 4: Tạo bảng kết quả**

* Kết hợp `user_id` và `score`:

```python
result_df = pd.DataFrame({
    'user_id': candidate_users,
    'score': scores
}).sort_values(by='score', ascending=False)
```

* Nếu bạn cần top `n` người:

```python
top_candidates = result_df.head(request.num_of_emp)
```

---

### **Bước 5: Loại trừ user đang bận**

```python
top_candidates = top_candidates[~top_candidates['user_id'].isin(request.busy_ids)]
```

* Kết quả cuối cùng: danh sách user **đã rank, phù hợp với task mới**, top `num_of_emp`

---

### **Flow tóm tắt dưới dạng sơ đồ logic**

```
[Dataset 100k dòng] 
       │
       ▼
[Filter candidate users theo domain] 
       │
       ▼
[Compute user_stats: trung bình performance] 
       │
       ▼
[Build result_candidates DataFrame (n_user × 6 features)] 
       │
       ▼
[model.predict(result_candidates.drop('user_id'))] 
       │
       ▼
[Combine user_id + score → sort theo score] 
       │
       ▼
[Exclude busy_ids] 
       │
       ▼
[Return top n_user recommendations]
```

---

### **Key point**

* `.fit()` đã học mối quan hệ giữa **user performance + task features → user_id**
* `.predict()` cần **đầy đủ feature như khi train**
* Nếu bạn chỉ điền `on_time=1, free_time=1, late_time=0` → tất cả users đều có score giống nhau → mất khả năng rank
