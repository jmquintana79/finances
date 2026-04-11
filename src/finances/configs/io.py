# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2026-03-28 23:34:49
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2026-04-11 21:46:21

import os

import finances.configs.env as penv

""" input folders """

# historical / raw
folder_raw = os.path.join(penv.FOLDER_DATA, "historical", "raw")
folder_raw_FinanceDatabase_symbols = os.path.join(folder_raw, "FinanceDatabase", "symbols")
# historical / processed
folder_processed = os.path.join(penv.FOLDER_DATA, "historical", "processed")
folder_symbols = os.path.join(folder_processed, "symbols")

""" data paths symbols """

# historical / raw / symbols
path_FinanceDatabase_symbols_etfs = os.path.join(
    folder_raw_FinanceDatabase_symbols, "symbols_FinanceDatabase_etfs.csv"
)
path_FinanceDatabase_symbols_indices = os.path.join(
    folder_raw_FinanceDatabase_symbols, "symbols_FinanceDatabase_indices.csv"
)
path_FinanceDatabase_symbols_funds = os.path.join(
    folder_raw_FinanceDatabase_symbols, "symbols_FinanceDatabase_funds.csv"
)
# historical / processed / symbols
path_symbols_FinanceDatabase = os.path.join(folder_symbols, "symbols_FinanceDatabase.csv")
