# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2026-03-28 23:34:49
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2026-04-11 21:16:23

import logging
import os

import pandas as pd

import finances.configs.io as pio

# logging by screen
logging.basicConfig(level=logging.INFO)


def save() -> None:
    """Load symbols from 'FinanceDatabase' and load in local

    Source: https://github.com/JerBouma/FinanceDatabase
    """
    try:
        # initialize output paths
        path_etfs = pio.path_FinanceDatabase_symbols_etfs
        path_indices = pio.path_FinanceDatabase_symbols_indices
        path_funds = pio.path_FinanceDatabase_symbols_funds
        # check if it already exist
        exits_etfs = os.path.exists(path_etfs)
        exits_indices = os.path.exists(path_indices)
        exits_funds = os.path.exists(path_funds)
        if exits_etfs and exits_indices and exits_funds:
            # display
            logging.warning("Symbols from 'FinanceDatabase' already exist")
            # return
            return None
        else:
            # display
            logging.info("Saving symbols files from 'FinanceDatabase'...")
            # load symbols
            etfs = pd.read_csv(
                "https://github.com/JerBouma/FinanceDatabase/blob/main/database/etfs.csv?raw=true",
                index_col=0,
            )
            indices = pd.read_csv(
                "https://github.com/JerBouma/FinanceDatabase/blob/main/database/indices.csv?raw=true",
                index_col=0,
            )
            funds = pd.read_csv(
                "https://github.com/JerBouma/FinanceDatabase/blob/main/database/funds.csv?raw=true",
                index_col=0,
            )
            # validate loaded data
            num_etfs = len(etfs)
            num_indices = len(indices)
            num_funds = len(funds)
            if (num_etfs == 0) or (num_indices == 0) or (num_funds == 0):
                # display
                logging.error(
                    f"Any loaded symbols file from 'FinanceDatabase' is empty: {num_etfs} {num_indices} {num_funds}"
                )
                # return
                return None
            else:
                # display
                logging.info(
                    f"Loaded symbols file from 'FinanceDatabase': {num_etfs} {num_indices} {num_funds}"
                )
                # save
                etfs.reset_index(drop = False).to_csv(path_etfs, index=False)
                indices.reset_index(drop = False).to_csv(path_indices, index=False)
                funds.reset_index(drop = False).to_csv(path_funds, index=False)
                # display
                logging.info("Saved symbols files from 'FinanceDatabase'")
                # return
                return None
    except Exception:
        # display
        logging.exception("saving symbols from 'FinanceDatabase'")


def main():
    # save symbols
    save()
    # return
    return None


if __name__ == "__main__":
    main()
