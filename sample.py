#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
WIP for EBNF parser of openCypher queries.
"""

import pathlib

from icecream import ic
from lark import Lark


if __name__ == "__main__":
    ebnf_path = pathlib.Path("grammar") / "lark-cypher.ebnf"
    grammar = ebnf_path.open().read()
    lalr = Lark(grammar)

    query = """
MATCH(p:Person)
RETURN p
LIMIT 1
    """.strip()

    parse = lalr.parse(query)
    ic(parse)
