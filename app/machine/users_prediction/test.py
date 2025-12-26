import numpy as np
import pandas as pd
from matplotlib import pyplot as plt

from app.machine.users_prediction.model import RecModelSvc
from app.util.constants.UserPrediction import CstTask, CstFiles


class RecModelTestSvc:
    @classmethod
    def plot_top_k_accuracy(cls, results, k_list):
        print("\n".join([
            f"{k}: {v}"
            for k, v in results.items()
        ]))

        ks = []
        accs = []

        for k in k_list:
            key = f"top_{k}_accuracy"
            if key in results:  # an toàn
                ks.append(k)
                accs.append(results[key])

        plt.figure(figsize=(7, 5))
        plt.plot(ks, accs, marker="o")
        plt.xlabel("k")
        plt.ylabel("Top-k Accuracy")
        plt.title("Top-k Accuracy Curve")
        plt.xticks(ks)
        plt.grid(True)
        plt.show()

    @classmethod
    def plot_true_rank_histogram(cls, result, max_rank=20, total_samples=None):
        true_ranks = result["true_ranks"]

        if total_samples is None:
            total_samples = len(true_ranks)

        ranks = [r for r in true_ranks if r <= max_rank]
        topk_count = len(ranks)

        plt.figure(figsize=(9, 5))
        plt.hist(
            ranks,
            bins=np.arange(1, max_rank + 2) - 0.5,
            edgecolor="black"
        )

        plt.xticks(range(1, max_rank + 1))
        plt.xlabel("Rank position of true label")
        plt.ylabel("Number of samples")
        plt.title(
            f"True Label Rank Distribution (Top {max_rank})\n"
            f"Top-{max_rank}: {topk_count}/{total_samples} "
            f"({topk_count / total_samples:.2%})"
        )

        plt.grid(axis="y", alpha=0.3)
        plt.show()

    @classmethod
    def _top_k_accuracy_test(cls, k_list) -> dict:
        df_test = pd.read_csv(CstFiles.TEST_DATA_FILE)
        df_test = RecModelSvc.pre_handle_dataset(df_test)

        X_test = df_test.drop(columns=[CstTask.label_name])
        labels = df_test[CstTask.label_name]

        label_encoder = RecModelSvc.load_encoder()
        y_test = label_encoder.transform(labels)

        model = RecModelSvc.load_model()
        proba = model.predict_proba(X_test)

        results = {}

        # -------- containers --------
        topk_correct = {k: 0 for k in k_list}
        true_ranks = []

        # -------- single loop --------
        for i in range(len(y_test)):
            ranked_idx = np.argsort(proba[i])[::-1]
            true_rank = np.where(ranked_idx == y_test[i])[0][0] + 1
            true_ranks.append(true_rank)

            for k in k_list:
                if true_rank <= k:
                    topk_correct[k] += 1

        # -------- accuracy --------
        for k in k_list:
            results[f"top_{k}_accuracy"] = topk_correct[k] / len(y_test)

        # -------- extra info for plotting --------
        results["true_ranks"] = true_ranks
        results["num_samples"] = len(y_test)

        return results

    @classmethod
    def run_test_loss(cls, k_list):
        # RecModelSvc.start_server()

        results = cls._top_k_accuracy_test(k_list)
        print("\n".join([
            f"{k}: {v}"
            for k, v in results.items()
        ]))
        return results

k_list = [1, 3, 5, 10, 30, 45]
RecModelSvc.start_server()
result = RecModelTestSvc.run_test_loss(k_list)
RecModelTestSvc.plot_top_k_accuracy(result, k_list)
RecModelTestSvc.plot_true_rank_histogram(
    result,
    max_rank=k_list[-1],
    total_samples=result["num_samples"]
)