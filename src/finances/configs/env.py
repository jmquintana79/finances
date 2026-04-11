# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2026-03-28 23:34:49
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2026-04-11 16:13:09

"""
Main folders root-folder definition (project, data, logs, outputs)

Normally data, outputs and logs folders are inside of folder project.
However it is not true always. For this reason I give the possibility
to define them individualy.
"""

import os
from pathlib import Path

FOLDER_PROJECT = Path(__file__).resolve().parents[3]
FOLDER_DATA = os.path.join(FOLDER_PROJECT, "data")
