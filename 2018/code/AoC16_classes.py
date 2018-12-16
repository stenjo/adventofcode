# Advent of Code 2018: https://adventofcode.com/2018/day/15
#
# Classes

import datetime, time
from datetime import timedelta
import pprint
import collections


class OpCodes():
    def __init__(self):
        self._before = [[]]
        self._codes  = [[]]
        self._after  = [[]]

        # Before: [3, 3, 2, 1]
        # 0 3 1 2
        # After:  [3, 3, 1, 1]

        # Before: [3, 2, 2, 1]
        # 5 3 2 1
        # After:  [3, 1, 2, 1]
    def load(self,data):
        index = 0
        for line in data:
            continue

    def findSamples(self):
        return 0

