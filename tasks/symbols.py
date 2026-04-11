# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2026-04-11 16:19:27
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2026-04-11 16:32:29

from finances.io.datasets.FinanceDatabase.symbols import save as save_fd
from invoke.context import Context
from invoke.tasks import task


@task
def save(ctx: Context) -> None:
    """Load symbol signals and save in local"""
    # save symbols from FinanceDatabase
    save_fd()
