# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2026-04-18 22:39:58
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2026-04-18 23:19:43

import os

import pandas as pd

import finances.configs.io as pio
from finances.configs.symbols import favorites


def load(with_only_favorites: bool = False) -> pd.DataFrame:
    """
    Loads the symbols dataset.

    Returns:
        pd.DataFrame: The symbols dataset.
    """
    # input folder
    folder_input = os.path.join(pio.folder_processed, "symbols")
    # list of files in the input folder
    files_input = os.listdir(folder_input)
    # check if files input list is empty
    if len(files_input) == 0:
        raise ValueError(f"No files found in the input folder: {folder_input}")
    # load and append all files in the input folder
    df_list = []
    for file in files_input:
        path_file = os.path.join(folder_input, file)
        df_file = pd.read_csv(path_file)
        df_list.append(df_file)
    # concatenate all dataframes in the list
    df = pd.concat(df_list, ignore_index=True, axis=0)
    # validate if the concatenated dataframe is empty
    if df.empty:
        raise ValueError(
            f"The concatenated dataframe is empty. Check the input files in the folder: {folder_input}"
        )
    # sort values by "symbol" column
    df = df.sort_values(by="symbol", ascending=True)
    # drop duplicates according to the "symbol" column
    df = df.drop_duplicates(subset="symbol", keep="first")
    # reset index
    df = df.reset_index(drop=True)
    # filter only favorites if the flag is True
    if with_only_favorites:
        df = df[df["symbol"].isin(favorites)].reset_index(drop=True)
    # validate if the filtered dataframe is empty
    if with_only_favorites and df.empty:
        raise ValueError(
            "The filtered dataframe is empty. Check the favorites list and the input files."
        )
    # return
    return df


def main():
    df = load(with_only_favorites=True)
    print(df.head())


if __name__ == "__main__":
    main()
