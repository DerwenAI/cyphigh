# CyPhigh

Support for distributed processing of `openCypher` in Python.


## Setup

```bash
python3 -m venv venv
source venv/bin/activate
python3 -m pip install -U pip
python3 -m pip install -r requirements.txt
```

## Dependencies

| dependency | version | license |
| --- | --- | --- |
| [`lark`](https://lark-parser.readthedocs.io/) | >= 1.1 | MIT |
| [`cypher.ebnf`](https://opencypher.org/resources/) | >= M18 | ASL 2 |

Note that `lark` uses a "modified EBNF" grammar format, so the EBNF
from `openCypher` had to be adapted.


## Resources

  * [`openCypher`](https://opencypher.org/)
  * ["Querying Property Graphs with [open]Cypher"](https://web.stanford.edu/class/cs520/abstracts/selmer-v3.pdf)

  * ["Parsing in Python"](https://tomassetti.me/parsing-in-python/)
  * [`libcypher-parser-python`](https://github.com/inonit/libcypher-parser-python)
  * [`grand-cypher`](https://github.com/aplbrain/grand-cypher)
  * [`globality/openCypher`](https://github.com/globality-corp/opencypher/)
