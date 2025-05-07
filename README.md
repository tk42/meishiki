# Meishiki

[![Python test](https://github.com/tk42/meishiki/actions/workflows/test.yml/badge.svg)](https://github.com/tk42/meishiki/actions/workflows/test.yml) ![Python 3.7](https://img.shields.io/badge/python-3.7-00af00.svg) [![PyPI](https://img.shields.io/pypi/v/meishiki)](https://pypi.org/project/meishiki/) ![License: MIT](https://img.shields.io/badge/license-MIT-a000ff.svg) ![CodeStyle: black](https://img.shields.io/badge/code%20style-black-000000.svg)

## Requirement

- Python >= 3.7
- jinja2
- pyyaml
- python-box

## Quickstart

```bash
$ pip install meishiki
```

Then,

```bash
$ python3 ./generate_html.py YYYY-MM-DD HH:MM SEX
```

SEX should be specified when male = 0, female = 1

## How to run MCP server

This library is supported MCP server.

```bash
$ python3 -m venv .venv
$ source .venv/bin/activate
$ pip install meishiki fastmcp
$ python3 ./mcp_server.py
```

and add the following to your ClaudeDesktop



## Run tests

```bash
$ pip install -e .
$ pytest --cov=meishiki ./test
```

## TODO

- [ ] 逆引きテーブル作成

## Thanks

@hajime-f/meishiki
