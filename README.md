
# pick

[![image](https://github.com/aisk/pick/actions/workflows/ci.yml/badge.svg)](https://github.com/aisk/pick/actions/workflows/ci.yml)
[![PyPI](https://img.shields.io/pypi/v/pick.svg)](https://pypi.python.org/pypi/pick)
[![PyPI](https://img.shields.io/pypi/dm/pick)](https://pypi.python.org/pypi/pick)

**pick** is a small python library to help you create curses based
interactive selection list in the terminal.

|         Basic          |         Multiselect          |
| :--------------------: | :--------------------------: |
| ![](example/basic.gif) | ![](example/multiselect.gif) |

## Installation

    $ pip install pick

## Usage

**pick** comes with a simple api:

    >>> from pick import pick

    >>> title = 'Please choose your favorite programming language: '
    >>> options = ['Java', 'JavaScript', 'Python', 'PHP', 'C++', 'Erlang', 'Haskell']
    >>> option, index = pick(options, title)
    >>> print(option)
    >>> print(index)

**outputs**:

    >>> C++