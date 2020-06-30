__all__ = ['render', 'Column', 'Table']


def render(headers, matrix):
    """return a string with markdown table (one-line cells only)"""
    def line1(string):
        return string.splitlines()[0] if string.splitlines() else ''

    def one_line_cells(cells, headers):
        cells = list(map(lambda s: line1(s).lstrip().rstrip(), cells))
        if len(cells) != len(headers):
            err_msg = """different length of headers (%s) and row cells (%s):
%s
%s""" % (len(headers), len(cells), "|".join(headers), "|".join(cells))
            raise ValueError(err_msg)
        return cells

    headers = list(map(lambda s: line1(s).lstrip().rstrip(), headers))
    separators = []
    for i in range(0, len(headers)):
        separators.append("-")
    matrix = list(map(lambda cols: one_line_cells(cols, headers), matrix))
    lines = ["|".join(headers), "|".join(separators)] + \
        list(map(lambda r: "|".join(r), matrix))
    return "\n".join(lines)


class Column:
    """attrs: `header`, `align` (`left`, `center`, `right`)"""
    align = "left"

    def __init__(self, header, align="left"):
        self.header = header
        self.align = align if align else "left"

    def __str__(self):
        return self.header

    def __repr__(self):
        return self.__str__()


class Table:
    """attrs: `columns`, `matrix`. methods: `getheaders()`, `getseparators()`, `getmatrix()`, `render()`"""
    columns = None
    matrix = None

    def __init__(self, columns, matrix):
        self.columns = list(columns)
        self.matrix = list(matrix)

    def getheaders(self):
        """return a list of headers"""
        return self.columns

    def getseparators(self):
        """return a list of separators"""
        values = []
        for column in self.columns:
            align = getattr(column, "align", "left")
            value = dict(left="-", center=":-:", right="-:").get(align, "-")
            values.append(value)
        return values

    def getmatrix(self):
        """return a matrix with data"""
        return self.matrix

    def render(self):
        """return a string with markdown table (if data not empty)"""
        matrix = self.getmatrix()
        if not matrix:
            return ""
        lines = ["|".join(self.getheaders()), "|".join(
            self.getseparators())] + list(map(lambda r: " |".join(r), matrix))
        return "\n".join(lines)

    def __bool__(self):
        return len(self.getmatrix()) > 0

    def __nonzero__(self):
        return self.__bool__()

    def __str__(self):
        return self.render()

    def __repr__(self):
        return self.__str__()
