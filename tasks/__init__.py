# -*- coding: utf-8 -*-
# @Author: Juan Quintana
# @Date:   2026-03-28 23:34:49
# @Last Modified by:   Juan Quintana
# @Last Modified time: 2026-04-11 22:00:09

from invoke import Collection

from . import data, devops

# add submodule as a collection
ns = Collection()
ns.add_collection(devops)
ns.add_collection(data)
