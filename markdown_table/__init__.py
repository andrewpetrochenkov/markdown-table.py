#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import public


@public.add
class Column:
    """column class. attrs: `header`, `align` (`left`, `center`, `right`)"""
    align = "left"

    def __init__(self, header, align="left"):
        self.header = header
        self.align = align if align else "left"

    def __str__(self):
        return self.header

    def __repr__(self):
        return self.__str__()


@public.add
class Table:
    """table class. attrs: `columns`, `data`"""
    columns = []
    data = []

    def __init__(self, columns, data):
        self.columns = list(columns)
        self.data = list(data)

    def get_headers(self):
        return self.columns

    def get_alignments(self):
        values = []
        for column in self.columns:
            align = getattr(column, "align", "left")
            value = dict(left="-", center=":-:", right="-:").get(align, "-")
            values.append(value)
        return values

    def get_data(self):
        return self.data

    def render(self):
        """return a string with markdown table (if data not empty)"""
        if not self.get_data():
            return ""
        return "\n".join([
            "|".join(self.get_headers()),
            "|".join(self.get_alignments()),
        ] + list(map(lambda r: " |".join(r), self.get_data())))

    def save(self, path):
        """save markdown table to a file"""
        dirname = os.path.dirname(path)
        if not dirname and not os.path.exists(dirname):
            os.makedirs(dirname)
        open(path, "w").write(str(self))

    def __bool__(self):
        return len(self.get_data()) > 0

    def __nonzero__(self):
        return self.__bool__()

    def __str__(self):
        return self.render()

    def __repr__(self):
        return self.__str__()
