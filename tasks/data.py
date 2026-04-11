# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2026-04-11 16:19:27
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2026-04-11 22:02:04

from finances.data.FinanceDatabase.cleaning.symbols import raw_to_processed as raw_to_processed_fd
from finances.data.FinanceDatabase.downloader.symbols import save as save_fd
from invoke.context import Context
from invoke.tasks import task


@task
def symbols(ctx: Context) -> None:
    """Collect symbols data

    In this process will be included different sources and
    process:
    - downloading
    - cleaning
    """

    ## FinanceDatabase

    # save symbols from
    save_fd()
    # raw to processed from FinanceDatabase
    raw_to_processed_fd()
