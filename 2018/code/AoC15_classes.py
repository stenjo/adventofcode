# Advent of Code 2018: https://adventofcode.com/2018/day/15
#
# Classes

import datetime, time
from datetime import timedelta
import pprint
import collections


class BeverageBandidts():
    recipes = []
    _index = 0
    def __init__(self):
        self.recipes.clear()

    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, i):
        self._index = i%len(i)

    def getScores(self):
        return 0


