#!/usr/bin/env python
# -*- coding: utf-8 -*-
import markdown_table


columns = ["name","__doc__"]
matrix = [
    ["name1","desc1"],
    ["name2","desc2"],
]
table = markdown_table.Table(columns,matrix)
print(str(table))

