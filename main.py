# coding=utf-8
# Copyright 2014 Pants project contributors (see CONTRIBUTORS.md).
# Licensed under the Apache License, Version 2.0 (see LICENSE).

from __future__ import absolute_import, division, print_function, unicode_literals

import sys


if __name__ == '__main__':
  greetees = sys.argv[1:] or ['world']
  for greetee in greetees:
    print('hello people')
