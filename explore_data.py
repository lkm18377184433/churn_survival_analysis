# -*- coding: utf-8 -*-
# @TIME    : 2022/2/16 9:22
# @AUTHOR  : liangkaimeng
# @SOFTWARE: PyCharm

import warnings
from pandas import read_csv
from pandas import DataFrame
from pandas import set_option

warnings.filterwarnings("ignore")
set_option("display.width", 10000)
set_option("display.max_rows", None)
set_option("display.max_columns", None)


if __name__ == "__main__":
    path = "data/train.csv"
    data = read_csv(path)
