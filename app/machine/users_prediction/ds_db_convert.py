import pandas as pd

from dataclasses import dataclass
from typing import Dict, Tuple
from datetime import datetime, timedelta

from app.util.constants.DBConvertor import BE_PROJECTS, FE_PROJECTS, QA_PROJECTS, HR_PROJECTS, BA_PROJECTS, SQL_PROJ, \
    SQL_PHASE, SQL_PROJ_ROLE, SQL_COL, SQL_TASK, SQL_TFU, SQL_REPORT
from app.util.constants.UserPrediction import CstFiles
from app.util.constants.UserPrediction import CstTaskConvertor

DATA = "D:\\Develop\\My_Own_Projects\\intern_project\\fastapi\\app\\storage\\data\\user_pred_ds.csv"
SQL_ROOT_PATH = "D:\\Develop\\My_Own_Projects\\intern_project\\fastapi\\app\\storage\\_ignored\\users_prediction\\sql"
"""
    1. Có một Project > 1 Phase > 1 Collection
    2. Separate Dataset 20,000 lines to:
        > Level (4 ~ 5,000)     > Priority (4 ~ 1,250)  > Domain { BE: 60, FE: 50, TEST: 30, BA: 5, HR: 5 }
"""
profiles: Dict[str, Dict[str, Tuple[int, int]]] = {
    "BACKEND": {
        "senior": (1, 20),
        "junior": (21, 50),
        "fresher": (51, 60)
    },
    "FRONTEND": {
        "senior": (61, 75),
        "junior": (76, 105),
        "fresher": (106, 110)
    },
    "TEST": {
        "senior": (111, 115),
        "junior": (116, 135),
        "fresher": (136, 140)
    },
    "HR": {
        "senior": (141, 143),
        "junior": (144, 145)
    },
    "BUSINESS_ANALYSIS": {
        "senior": (146, 146),
        "junior": (147, 149),
        "fresher": (150, 150)
    }
}


@dataclass(frozen=True)
class UserProfile:
    user_id: int
    domain: str
    level: str


@dataclass(frozen=True)
class TaskUserRow:
    user_id: int
    started: datetime
    submitted: datetime

tasks = []
def aggregate_tasks():
    global tasks, DATA
    df_full = pd.read_csv(DATA)
    domains = profiles.keys()

    for level in CstTaskConvertor.enc_levels:
        df_level = df_full[df_full["level"] == level]

        for prior in CstTaskConvertor.enc_priorities:
            df_level_prior = df_level[df_level["priority"] == prior]

            for domain in domains:
                df = df_level_prior[df_level_prior["domain"] == domain]

                user_statistic = {}
                for record in df.itertuples():
                    if record.user_id not in user_statistic:
                        user_statistic[record.user_id] = [record]
                    else:
                        user_statistic[record.user_id].append(record)

                users = user_statistic.keys()
                while len(users) != 0:
                    current_batch = []
                    temp_ids = list(user_statistic.keys())
                    for user_id in temp_ids:
                        current_batch.append(user_statistic[user_id].pop())
                        if len(user_statistic[user_id]) == 0:
                            del user_statistic[user_id]

                    tasks.append(current_batch)
                    users = user_statistic.keys()

aggregate_tasks()

def print_out(tss: list):
    for period in tss:
        if type(period[0]) == list:
            print([[
                u.user_id for u in t
            ] for t in period])
        else:
            print([t.user_id for t in period])

def print_out_domains(tss: list):
    for period in tss:
        if type(period[0]) == list:
            print([set([
                u.domain for u in t
            ]) for t in period])
        else:
            print(set([t.domain for t in period]))

def can_be_same_periods(a: list[int], b: list[int], c: list[int], d: list[int]) -> bool:
    return len(set(a + b + c + d)) == len(a) + len(b) + len(c) + len(d)

def can_be_same_period(a: list[int], b: list[int]) -> bool:
    return len(set(a + b)) == len(a) + len(b)

def aggregate_period_double_task(
    periods_pair: list,
    periods: list,
    left: list,
    right: list
):
    for i in range(0, len(left)):
        [a, b] = left[i]
        [c, d] = right[i]
        if can_be_same_periods(
            [t.user_id for t in a],
            [t.user_id for t in b],
            [t.user_id for t in c],
            [t.user_id for t in d]
        ):
            periods_pair.append([a, b, c, d])
        else:
            periods.append(left[i])
            periods.append(right[i])


def aggregate_period_single_task(
    periods_pair: list,
    periods: list,
    left: list,
    right: list
):
    for i in range(0, len(left)):
        if can_be_same_period(
            [t.user_id for t in left[i]],
            [t.user_id for t in right[i]]
        ):
            periods_pair.append([left[i], right[i]])
        else:
            periods.append([left[i]])
            periods.append([right[i]])

def aggregate_fit_tasks_in_period(ts: list):
    tss = sorted(ts, key=lambda t: len(t), reverse=True)
    tss_len = len(tss)

    if tss_len % 2 == 1:
        # 100/2 = 50 = [0-49; 51-100]
        mid_idx = tss_len // 2
        left = tss[:mid_idx]
        mid = [tss[mid_idx]]
        right = list(reversed(tss[mid_idx + 1:]))
    else:
        # 99/2 = 49.5 = [0-49; 50-100]
        mid_idx = tss_len // 2
        left = tss[0:mid_idx]
        mid = []
        right = list(reversed(tss[mid_idx:]))

    periods = []
    periods_pair = []

    if type(left[0][0]) == list:
        aggregate_period_double_task(periods_pair, periods, left, right)

    if type(left[0][0]) != list:
        aggregate_period_single_task(periods_pair, periods, left, right)

    bad_result = []
    bad_result.extend(mid)
    bad_result.extend(periods)
    return periods_pair, bad_result

filtered_tasks = {
    'BACKEND': [],
    'FRONTEND': [],
    'TEST': [],
    'HR': [],
    'BUSINESS_ANALYSIS': [],
}

for t in tasks:
    if t[0].domain == 'BACKEND':
        filtered_tasks['BACKEND'].append(t)
    elif t[0].domain == 'FRONTEND':
        filtered_tasks['FRONTEND'].append(t)
    elif t[0].domain == 'TEST':
        filtered_tasks['TEST'].append(t)
    elif t[0].domain == 'HR':
        filtered_tasks['HR'].append(t)
    elif t[0].domain == 'BUSINESS_ANALYSIS':
        filtered_tasks['BUSINESS_ANALYSIS'].append(t)

agg_task_be, bad_tasks_be1 = aggregate_fit_tasks_in_period(filtered_tasks['BACKEND'])
agg_task_be.extend(bad_tasks_be1)

agg_task_fe, bad_tasks_fe1 = aggregate_fit_tasks_in_period(filtered_tasks['FRONTEND'])
agg_task_fe.extend(bad_tasks_fe1)

agg_task_te, bad_tasks_te1 = aggregate_fit_tasks_in_period(filtered_tasks['TEST'])
agg_task_te.extend(bad_tasks_te1)

agg_task_hr, bad_tasks_hr1 = aggregate_fit_tasks_in_period(filtered_tasks['HR'])
agg_task_hr.extend(bad_tasks_hr1)

agg_task_ba, bad_tasks_ba1 = aggregate_fit_tasks_in_period(filtered_tasks['BUSINESS_ANALYSIS'])
agg_task_ba.extend(bad_tasks_ba1)

print(f"BE-{len(agg_task_be)}-{sum([
    sum([len(t) for t in ts])
    for ts in agg_task_be])}")
print(f"FE-{len(agg_task_fe)}-{sum([
    sum([len(t) for t in ts])
    for ts in agg_task_fe])}")
print(f"TE-{len(agg_task_te)}-{sum([
    sum([len(t) for t in ts])
    for ts in agg_task_te])}")
print(f"HR-{len(agg_task_hr)}-{sum([
    sum([len(t) for t in ts])
    for ts in agg_task_hr])}")
print(f"BA-{len(agg_task_ba)}-{sum([
    sum([len(t) for t in ts])
    for ts in agg_task_ba])}")

def fmt_d(t: datetime) -> str:
    return t.strftime("%Y-%m-%d")

def fmt_t(t: datetime) -> str:
    return t.strftime("%Y-%m-%d %H:%M:%S.%f")

def save_query_in_txt(formatted_query: str, path_tail: str):
    import time
    global SQL_ROOT_PAT
    with open(SQL_ROOT_PATH + f"\\task_{path_tail}.sql", "w", encoding="utf-8") as f:
        f.write(formatted_query)

GLOBAL_PM = 154
GLOBAL_LEAD = 151
PROJECT_ID = 1
PROJ_ROLE_ID = 1
PHASE_ID = 1
COLLECTION_ID = 1
TASK_ID = 1
TFU_ID = 1
REV_LEVEL = {v: k for k, v in CstTaskConvertor.map_levels.items()}
REV_PRIORITY = {v: k for k, v in CstTaskConvertor.map_priorities.items()}

def start_generate_query(tss: list, proj_info: dict, path_tail: str):
    root_date = datetime(2020, 1, 1, 0, 0, 0, 0)
    flat_tss = []
    for ts in tss:
        temp = []
        for t in ts:
            if str(type(t[0])) != "<class 'pandas.core.frame.Pandas'>":
                temp.append(t)
            else:
                temp.extend(t)
        flat_tss.append(temp)
    print(f"Flat-tasks = {len(flat_tss)}")

    r_times = {}
    for proj_name, phases in proj_info.items():
        r_times[proj_name] = {"start": root_date, "end": None}
        root_date += timedelta(minutes=5)

        last_phase_t = None
        for phase_name, collections in phases.items():
            r_times[proj_name][phase_name] = {"start": root_date, "end": None}
            root_date += timedelta(minutes=5)

            last_col_t = None
            for col_name, tasks in collections.items():
                r_times[proj_name][phase_name][col_name] = {"start": root_date, "end": None}
                root_date += timedelta(minutes=5)

                last_task_t = None
                for task_name, task_node in tasks.items():
                    idx = int(task_node["start"].split("_")[1]) - 1
                    tfus = flat_tss[idx]
                    if type(tfus) != list:
                        f_task = tfus
                    else:
                        f_task = tfus[0]

                    task_node["domain"] = f_task.domain
                    task_node["level"] = f_task.level
                    task_node["priority"] = f_task.priority

                    root_date += timedelta(days=1)
                    task_node["start"] = root_date

                    total_date = f_task.level + f_task.priority
                    root_date += timedelta(days=total_date)
                    task_node["dead"] = root_date

                    total_sec = total_date*24*60*60
                    task_node["tfu"] = []
                    """
                        1. Sớm thì tính như bth
                        2. Trễ thì mặc định chia đôi thời gian dùng:
                            + Nếu thời gian dùng < 2.
                                + Nửa trước (tính từ dead) là lúc bắt đầu
                                + Nửa sau (tính từ dead) là lúc nộp
                            + Nếu thời gian dùng >=2.
                                + Mặc định bắt đầu sau 0.1 times, và cứ thế tính.
                    """
                    end_t = None
                    for t in tfus:
                        if t.is_on_time == 1:   # free + used <= 1
                            submit_t = root_date - timedelta(seconds=total_sec * t.free_time_rto)
                            start_t = submit_t - timedelta(seconds=total_sec * t.used_time_rto)
                        else:
                            if t.used_time_rto < 2:
                                half_of_used = t.used_time_rto / 2
                                start_t = root_date - timedelta(seconds=total_sec * half_of_used)
                                submit_t = root_date + timedelta(seconds=total_sec * half_of_used)
                            else:
                                start_t = root_date - timedelta(seconds=total_sec * 0.1) # default after 0.1 times.
                                submit_t = start_t + timedelta(seconds=total_sec * t.used_time_rto)
                        t_d = t._asdict()
                        t_d["start"] = fmt_t(start_t)
                        t_d["submit"] = fmt_t(submit_t)
                        t_d["r_create"] = fmt_t(submit_t)
                        t_d["r_update"] = fmt_t(submit_t)
                        t_d["r_review"] = fmt_t(submit_t + timedelta(minutes=5))
                        if end_t is None:
                            end_t = submit_t + timedelta(minutes=5 + 5)
                        else:
                            end_t = max(end_t, submit_t + timedelta(minutes=5 + 5))
                        task_node["tfu"].append(t_d)
                    task_node["end"] = end_t
                    last_task_t = end_t

                last_col_t = last_task_t + timedelta(minutes=5)
                r_times[proj_name][phase_name][col_name]["end"] = last_col_t

            last_phase_t = last_col_t + timedelta(minutes=5)
            r_times[proj_name][phase_name]["end"] = last_phase_t

        r_times[proj_name]["end"] = last_phase_t + timedelta(minutes=5)

    result = "\nSTART TRANSACTION;"
    global PROJECT_ID, PROJ_ROLE_ID, PHASE_ID, COLLECTION_ID, TASK_ID, TFU_ID
    for proj_name, phases in proj_info.items():
        result += "\n" + SQL_PROJ(
            proj_id=PROJECT_ID, proj_name=proj_name, creator=GLOBAL_PM,
            created_t=fmt_t(r_times[proj_name]["start"]),
            start_d=fmt_d(r_times[proj_name]["start"]),
            due_d=fmt_d(r_times[proj_name]["end"]))

        result += "\n" + SQL_PROJ_ROLE(owner=GLOBAL_PM, o_id=PROJ_ROLE_ID, member=GLOBAL_LEAD, m_id=PROJ_ROLE_ID + 1, proj_id=PROJECT_ID)

        for phase_name, collections in phases.items():
            result += "\n" + SQL_PHASE(
                phase_id=PHASE_ID, proj_id=PROJECT_ID, phase_name=phase_name, creator=GLOBAL_PM,
                created_t=fmt_t(r_times[proj_name][phase_name]["start"]),
                start_d=fmt_d(r_times[proj_name][phase_name]["start"]),
                due_d=fmt_d(r_times[proj_name][phase_name]["end"]))

            for col_name, tasks in collections.items():
                result += "\n" + SQL_COL(
                    col_id=COLLECTION_ID, phase_id=PHASE_ID, col_name=col_name, creator=GLOBAL_PM,
                    created_t=fmt_t(r_times[proj_name][phase_name][col_name]["start"]),
                    start_d=fmt_d(r_times[proj_name][phase_name][col_name]["start"]),
                    due_d=fmt_d(r_times[proj_name][phase_name][col_name]["end"]))

                for task_name, task_node in tasks.items():
                    result += "\n" + SQL_TASK(
                        task_id=TASK_ID,
                        col_id=COLLECTION_ID,
                        task_name=task_name,
                        created_t=fmt_t(task_node['start']),
                        start_d=fmt_d(task_node['start']),
                        dead_d=fmt_d(task_node['dead']),
                        end_d=fmt_d(task_node['end']),
                        creator=GLOBAL_LEAD,
                        level=REV_LEVEL[task_node['level']],
                        ttype=task_node['domain'],
                        priority=REV_PRIORITY[task_node['priority']])

                    start_tfu_id = TFU_ID
                    tfu_query, TFU_ID = SQL_TFU(
                        TFU_ID=TFU_ID, task_id=TASK_ID,
                        task_create_at=fmt_t(task_node['start']), tfus=task_node['tfu'])
                    result += "\n" + tfu_query
                    result += "\n" + SQL_REPORT(TFU_ID=start_tfu_id, tfus=task_node['tfu'])

                    TFU_ID += 1
                    TASK_ID += 1

                COLLECTION_ID += 1

            PHASE_ID += 1

        PROJECT_ID += 1
        PROJ_ROLE_ID += 2

    result += f"""\n
ALTER TABLE project AUTO_INCREMENT = {PROJECT_ID};
ALTER TABLE project_role AUTO_INCREMENT = {PROJ_ROLE_ID};
ALTER TABLE `phase` AUTO_INCREMENT = {PHASE_ID};
ALTER TABLE collection AUTO_INCREMENT = {COLLECTION_ID};
ALTER TABLE task AUTO_INCREMENT = {TASK_ID};
ALTER TABLE task_for_users AUTO_INCREMENT = {TFU_ID};
ALTER TABLE report AUTO_INCREMENT = {TFU_ID};

COMMIT;
"""
    # print(r_times)
    # print(proj_info)

    save_query_in_txt(result, path_tail)

start_generate_query(agg_task_be, BE_PROJECTS, "BE")
start_generate_query(agg_task_fe, FE_PROJECTS, "FE")
start_generate_query(agg_task_te, QA_PROJECTS, "QA")
start_generate_query(agg_task_hr, HR_PROJECTS, "HR")
start_generate_query(agg_task_ba, BA_PROJECTS, "BA")
