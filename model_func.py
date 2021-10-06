import pandas as pd
import math
import scipy.stats as st

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 500)
pd.set_option('display.expand_frame_repr', False)
pd.set_option('display.float_format', lambda x: '%.2f' % x)


def bayesian_average_rating(n, confidence=0.95):
    if sum(n) == 0:
        return 0
    K = len(n)
    z = st.norm.ppf(1 - (1 - confidence) / 2)
    N = sum(n)
    first_part = 0.0
    second_part = 0.0
    for k, n_k in enumerate(n):
        first_part += (k + 1) * (n[k] + 1) / (N + K)
        second_part += (k + 1) * (k + 1) * (n[k] + 1) / (N + K)
    score = first_part - z * math.sqrt((second_part - first_part * first_part) / (N + K + 1))
    return score


def bayes_apply(dataframe):
    dataframe["bar_sorting_score"] = dataframe.apply(lambda x: bayesian_average_rating(x[["1_points",
                                                                                          "2_points",
                                                                                          "3_points",
                                                                                          "4_points",
                                                                                          "5_points"]]), axis=1)


def weighted_rating(r, v, M, C):
    return (v / (v + M) * r) + (M / (v + M) * C)


def weigthed_apply(dataframe, M=10):
    dataframe["weighted_rating_score"] = weighted_rating(dataframe["rating"], dataframe["vote_count"], M,
                                                         dataframe['rating'].mean())


def sort_bayes(dataframe, head=20):
    print(dataframe.sort_values("bar_sorting_score", ascending=False).head(head))


def sort_weighted(dataframe, head=20):
    print(dataframe.sort_values("weighted_rating_score", ascending=False).head(head))
