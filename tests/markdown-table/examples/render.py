#!/usr/bin/env python
# -*- coding: utf-8 -*-
import markdown_table


headers = ["name","__doc__"]
matrix = [
    ["name1","desc1"],
    ["name2","desc2"],
]
string = markdown_table.render(headers,matrix)
print(string)

