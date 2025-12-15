import sys
import os

import pandas as pd

from app.dto.task_user import RecommendingUsersRequest
from app.util.constants.UserPrediction import CstTaskConvertor, CstUser, CstFiles, CstTask
import matplotlib.pyplot as plt

class Tee:
    def __init__(self, filename, mode="a"):
        self.file = open(filename, mode, encoding="utf-8")
        self.stdout = sys.stdout
        self.stderr = sys.stderr

    def write(self, message):
        self.file.write(message)
        self.file.flush()          # ghi ngay
        os.fsync(self.file.fileno())
        self.stdout.write(message) # vẫn in ra terminal

    def flush(self):
        self.file.flush()
        self.stdout.flush()


class LossRecorder:
    def __init__(self):
        self.iterations = []
        self.losses = []

    def __call__(self, env):
        for data_name, eval_name, loss, _ in env.evaluation_result_list:
            if eval_name == "multi_logloss":
                self.iterations.append(env.iteration + 1)
                self.losses.append(loss)

class LossDebugger:

    @classmethod
    def plot_loss(cls, iterations, losses, save_path: str = None):
        plt.figure(figsize=(8, 5))
        plt.plot(iterations, losses, marker="o")
        plt.xlabel("Iteration")
        plt.ylabel("Multi Log Loss")
        plt.title("Training Loss Curve")
        plt.grid(True)

        if save_path:
            plt.savefig(save_path, dpi=150)

        plt.show()


class DebuggerSvc:
    tee = None

    @classmethod
    def log_request(cls, request: RecommendingUsersRequest):
        enc_req = CstTaskConvertor.encode_request(request)
        print("❓ QUESTION: Who are the best employees for a new task?")
        print(f"   - Domain:   {request.domain} - {CstTaskConvertor.map_domains[request.domain]}")
        print(f"   - Level:    {request.level} - {CstTaskConvertor.map_levels[request.level]}")
        print(f"   - Priority: {request.priority} - {CstTaskConvertor.map_priorities[request.priority]}")
        print("------------------------------------------------------")

    @classmethod
    def log_prediction(
            cls,
            recommendations: pd.DataFrame,
            user_map: dict[str, int],
            request: RecommendingUsersRequest,
            cache: dict[str, float],
            max_ids_num=-1
    ):
        enc_request = CstTaskConvertor.encode_request(request)

        if recommendations.empty:
            print("❗ ANSWER: No suitable employees were found for this request.")
            return

        print(f"🏆 ANSWER: Here are the top {len(recommendations)} recommendations:")

        max_ids_num = max_ids_num if max_ids_num != -1 else len(recommendations)
        for index, employee in enumerate(recommendations.itertuples(index=False), start=1):
            if index >= max_ids_num:
                break
            user_id = int(getattr(employee, CstUser.user_id))
            score = float(getattr(employee, CstUser.score))
            print(f"  {index}. User ID: {user_id:<4} with Score={score}")
            print("    Full Data:")

            dif_total = {
                CstUser.user_id: user_id,
                CstTask.level: 0,
                CstTask.priority: 0,
                CstTask.free_time_rto: 0,
                CstTask.used_time_rto: 0,
                "total_task": 0
            }
            user_tasks = user_map.get(user_id, [])
            for task in user_tasks:
                # --- Lấy dữ liệu gốc ---
                domain_val = task.get(CstTask.domain, "")
                level_val = float(task.get(CstTask.level, 0))
                priority_val = float(task.get(CstTask.priority, 0))
                is_on_time_val = float(task.get(CstTask.is_on_time, 0))
                free_time_val = float(task.get(CstTask.free_time_rto, 0))
                used_time_val = float(task.get(CstTask.used_time_rto, 0))

                # --- Tính độ lệch ---
                dif_level = abs(level_val - enc_request.level)
                dif_priority = abs(priority_val - enc_request.priority)

                # --- Tổng hợp diff ---
                dif_total["total_task"] += 1
                dif_total[CstTask.level] += dif_level
                dif_total[CstTask.priority] += dif_priority
                dif_total[CstTask.free_time_rto] += free_time_val
                dif_total[CstTask.used_time_rto] += used_time_val

                # --- Cache values ---
                max_free_time = cache.get("max_free_time", 0)
                min_used_time = cache.get("min_used_time", 0)

            #     # --- Print task ---
            #     print(
            #         f"      - user_id: {task.get('user_id', 'N/A')}, "
            #         f"domain: {domain_val} (dif={request.domain}), "
            #         f"level: {level_val} (dif={dif_level}), "
            #         f"priority: {priority_val} (dif={dif_priority}), "
            #         f"is_on_time: {is_on_time_val}, "
            #         f"free_time_rto: {free_time_val} (max={max_free_time}), "
            #         f"used_time_rto: {used_time_val} (min={min_used_time})"
            #     )

            # # --- Print summary dif ---
            # print(
            #     "        ↳ 🔹 Total dif",
            #     f"      - user_id: {dif_total[CstUser.user_id]}, "
            #     f"level: {dif_total[CstTask.level]:.2f}, "
            #     f"priority: {dif_total[CstTask.priority]:.2f}, "
            #     f"free_time: {dif_total[CstTask.free_time_rto]:.2f}, "
            #     f"used_time: {dif_total[CstTask.used_time_rto]:.2f}"
            # )
            # print(
            #     "        ↳ 🔹 Avg dif",
            #     f"      - user_id: {dif_total[CstUser.user_id]}, "
            #     f"level: {(dif_total[CstTask.level] / dif_total["total_task"]):.2f}, "
            #     f"priority: {(dif_total[CstTask.priority] / dif_total["total_task"]):.2f}, "
            #     f"free_time: {(dif_total[CstTask.free_time_rto] / dif_total["total_task"]):.2f}, "
            #     f"used_time: {(dif_total[CstTask.used_time_rto] / dif_total["total_task"]):.2f}, "
            #     f"total_task: {dif_total["total_task"]}"
            # )
            print("-" * 40)

        print("======================================================\n")

    @classmethod
    def start_terminal_log(cls):
        cls.tee = Tee(CstFiles.LOG_FILE)
        sys.stdout = cls.tee

    @classmethod
    def stop_terminal_log(cls):
        sys.stderr = cls.tee
        print(f"[LOGGER] Terminal log enabled → {CstFiles.LOG_FILE}")
        cls.tee.flush()

    @classmethod
    def get_user_map(cls, df: pd.DataFrame):
        user_map = {}
        for _, row in df.iterrows():
            uid = row[CstUser.user_id]
            next_elem = {
                CstUser.user_id: uid,
                CstTask.domain: row[CstTask.domain],
                CstTask.level: row[CstTask.level],
                CstTask.priority: row[CstTask.priority],
                CstTask.is_on_time: row[CstTask.is_on_time],
                CstTask.free_time_rto: row[CstTask.free_time_rto],
                CstTask.used_time_rto: row[CstTask.used_time_rto]
            }
            user_map.setdefault(uid, []).append(next_elem)
        return user_map