# -*- coding: utf-8 -*-
# @TIME    : 2022/2/15 16:42
# @AUTHOR  : liangkaimeng
# @SOFTWARE: PyCharm

"""
    提取用于建模的数据
"""
import warnings
from pandas import read_csv

warnings.filterwarnings("ignore")


def train_test_extract(filepath: str):
    data = read_csv(filepath, encoding="utf-8")

    isnull_count = data.isnull().sum() / data.shape[0]
    data = data[isnull_count[isnull_count < 0.7].index.tolist()]

    train = data[data["issue_d"].str.contains(".*2015|.*2016|.*2017", na=False)]
    test = data[data["issue_d"].str.contains(".*2018", na=False)]

    train.to_csv("data/train.csv", index=False, encoding="utf-8")
    test.to_csv("data/test.csv", index=False, encoding="utf-8")


if __name__ == "__main__":
    path = "data/accepted_2007_to_2018Q4.csv"
    train_test_extract(path)
