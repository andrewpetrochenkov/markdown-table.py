<!--
https://pypi.org/project/readme-generator/
-->

[![](https://img.shields.io/pypi/pyversions/markdown-table.svg?longCache=True)](https://pypi.org/project/markdown-table/)
[![](https://img.shields.io/pypi/v/markdown-table.svg?maxAge=3600)](https://pypi.org/project/markdown-table/)
[![Travis](https://api.travis-ci.org/looking-for-a-job/markdown-table.py.svg?branch=master)](https://travis-ci.org/looking-for-a-job/markdown-table.py/)

#### Classes
class|`__doc__`
-|-
`markdown_table.Column` |attrs: `header`, `align` (`left`, `center`, `right`)
`markdown_table.Table` |attrs: `columns`, `matrix`. methods: `getheaders()`, `getseparators()`, `getmatrix()`, `render()`

#### Functions
function|`__doc__`
-|-
`markdown_table.render(headers, matrix)` |return a string with markdown table (one-line cells only)

<p align="center">
    <a href="https://pypi.org/project/readme-generator/">readme-generator</a>
</p>