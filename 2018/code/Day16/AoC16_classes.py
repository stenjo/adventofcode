# Advent of Code 2018: https://adventofcode.com/2018/day/16
#
# Classes

import datetime, time
from datetime import timedelta
import pprint
import collections


class OpCodes():

    def __init__(self):
        self._register = [[],[],[],[]]
        self._before = []
        self._codes  = []
        self._after  = []

        # Before: [3, 3, 2, 1]
        # 0 3 1 2
        # After:  [3, 3, 1, 1]

        # Before: [3, 2, 2, 1]
        # 5 3 2 1
        # After:  [3, 1, 2, 1]
    def load(self,data):
        index = 0
        for i in range(len(data)):
            line = data[i]
            if line.strip().split(':')[0] == 'Before':
                self._before.append(eval(line.strip().split(':')[1]))
                self._after.append(eval(data[i+2].strip().split(':')[1]))
                self._codes.append(eval('['+data[i+1].strip().replace(' ',',')+']'))
                i += 2

    def findSamples(self):
        return 0

