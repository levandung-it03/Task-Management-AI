import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.metrics import average_precision_score, ndcg_score

from app.machine.users_prediction.model import RecModelSvc
from app.util.constants.UserPrediction import CstFiles, CstSymbols, CstTask


class RecModelTestSvc:

    @classmethod
    def dcg_at_k(cls, rels, k):
        rels = np.asarray(rels)[:k]
        return np.sum((2 ** rels - 1) / np.log2(np.arange(2, len(rels) + 2)))

    @classmethod
    def collect_ranking_metrics(cls, k_list=[3]):
        df_test = pd.read_csv(CstFiles.TEST_DATA_FILE)
        df_test = RecModelSvc.pre_handle_dataset(df_test)

        X_test = df_test.drop(columns=[CstTask.label_name])
        y_labels = df_test[CstTask.label_name].values

        model = RecModelSvc.load_model()
        label_encoder = RecModelSvc.load_encoder()

        class_labels = label_encoder.inverse_transform(model.classes_)
        proba = model.predict_proba(X_test)

        ndcg_per_k = {k: [] for k in k_list}
        map_scores = []
        samples_debug = []

        for i in range(len(X_test)):
            result = cls.analyze_single_sample(
                scores=proba[i],
                class_labels=class_labels,
                true_label=y_labels[i]
            )

            samples_debug.append(result)

            for k in k_list:
                ndcg = ndcg_score([result["relevance"]], [result["scores"]], k=k)
                ndcg_per_k[k].append(ndcg)

            binary_rel = (result["relevance"] == 1.0).astype(int)
            map_scores.append(
                average_precision_score(binary_rel, result["scores"])
            )

        return {
            "ndcg_per_k": ndcg_per_k,
            "map_scores": map_scores,
            "samples_debug": samples_debug
        }

    @classmethod
    def plot_true_rank_distribution(cls, metrics: dict, max_rank=20):
        ranks = [
            s["true_rank"]
            for s in metrics["samples_debug"]
            if s["true_rank"] <= max_rank
        ]

        plt.figure(figsize=(7, 5))
        sns.countplot(x=ranks)
        plt.xlabel("Rank position of true label")
        plt.title("True Label Rank Distribution (Top positions)")
        plt.grid(True)
        plt.show()

    @classmethod
    def plot_ndcg_distribution(cls, metrics: dict, k=3):
        plt.figure(figsize=(7, 5))
        sns.histplot(metrics["ndcg_per_k"][k], bins=30, kde=True)
        plt.xlabel(f"NDCG@{k}")
        plt.title(f"NDCG@{k} Distribution per Sample")
        plt.show()

    @classmethod
    def summarize_metrics(cls, metrics: dict):
        print("\n====== RANKING METRICS ======")
        for k, values in metrics["ndcg_per_k"].items():
            print(f"NDCG@{k}: {np.mean(values):.4f}")

        print(f"MAP: {np.mean(metrics['map_scores']):.4f}")

    @classmethod
    def analyze_single_sample(cls, scores, class_labels, true_label):
        relevance = np.zeros(len(class_labels))

        for idx, pred_label in enumerate(class_labels):
            if pred_label == true_label:
                relevance[idx] = 1.0

        ranked_idx = np.argsort(scores)[::-1]
        true_rank = np.where(class_labels[ranked_idx] == true_label)[0][0] + 1

        return {
            "scores": scores,
            "relevance": relevance,
            "ranked_idx": ranked_idx,
            "true_rank": true_rank
        }


metrics = RecModelTestSvc.collect_ranking_metrics(k_list=[3])
RecModelTestSvc.summarize_metrics(metrics)
RecModelTestSvc.plot_true_rank_distribution(metrics)