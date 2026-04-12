# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2026-04-11 16:19:27
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2026-04-12 18:50:18

from finances.data.AlphaVantage.cleaning.symbols import raw_to_processed as raw_to_processed_av
from finances.data.AlphaVantage.downloader.symbols import save as save_av
from finances.data.FinanceDatabase.cleaning.symbols import raw_to_processed as raw_to_processed_fd
from finances.data.FinanceDatabase.downloader.symbols import save as save_fd
from invoke.context import Context
from invoke.tasks import task


@task
def symbols(ctx: Context) -> None:
    """Collect symbols data

    In this process will be included different sources:
        - AlphaVantage
        - FinanceDatabase
    For each source, the following steps will be executed:
    and processes:
        - downloading
        - cleaning
    """

    ## FinanceDatabase

    # save symbols from
    save_fd()
    # raw to processed from FinanceDatabase
    raw_to_processed_fd()

    ## AlphaVantage

    # save symbols from AlphaVantage
    save_av()
    # raw to processed from AlphaVantage
    raw_to_processed_av()
