# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2026-03-28 23:34:49
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2026-04-12 14:30:29

import os

import finances.configs.env as penv

""" input folders """

# historical / raw
folder_raw = os.path.join(penv.FOLDER_DATA, "historical", "raw")
folder_raw_FinanceDatabase_symbols = os.path.join(folder_raw, "FinanceDatabase", "symbols")
folder_raw_AlphaVantage_symbols = os.path.join(folder_raw, "AlphaVantage", "symbols")

# historical / processed
folder_processed = os.path.join(penv.FOLDER_DATA, "historical", "processed")
folder_symbols = os.path.join(folder_processed, "symbols")

""" data paths symbols """

# historical / raw / symbols
path_raw_FinanceDatabase_symbols_etfs = os.path.join(
    folder_raw_FinanceDatabase_symbols, "symbols_FinanceDatabase_etfs.csv"
)
path_raw_FinanceDatabase_symbols_indices = os.path.join(
    folder_raw_FinanceDatabase_symbols, "symbols_FinanceDatabase_indices.csv"
)
path_raw_FinanceDatabase_symbols_funds = os.path.join(
    folder_raw_FinanceDatabase_symbols, "symbols_FinanceDatabase_funds.csv"
)
path_raw_AlphaVantage_symbols = os.path.join(
    folder_raw_AlphaVantage_symbols, "symbols_AlphaVantage.csv"
)
# historical / processed / symbols
path_processed_FinanceDatabase_symbols = os.path.join(folder_symbols, "symbols_FinanceDatabase.csv")
path_processed_AlphaVantage_symbols = os.path.join(folder_symbols, "symbols_AlphaVantage.csv")
