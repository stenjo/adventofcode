from collections import Counter, defaultdict
from itertools import zip_longest

from Day13.Mirror import Mirror


class Valley:
    def __init__(self, input):
        self.patterns = []
        pattern = []
        for line in input.strip().split("\n"):
            if len(line.strip()) > 0:
                pattern.append(line.strip())
            else:
                self.patterns.append(pattern)
                pattern = []
        if len(pattern):
            self.patterns.append(pattern)

    def rowsByColumnsSum(self):
        rows = filter(
            lambda x: x != None, [Mirror(r).findMirrorRow() for r in self.patterns]
        )
        cols = filter(
            lambda x: x != None, [Mirror(c).findMirrorCol() for c in self.patterns]
        )
        return sum(cols) + sum(rows) * 100

    def smudgedRowsByColumnsSum(self):
        rows = filter(
            lambda x: x != None, [Mirror(r).findCandidateRow() for r in self.patterns]
        )
        cols = filter(
            lambda x: x != None, [Mirror(c).findCandidateCol() for c in self.patterns]
        )
        return sum(cols) + sum(rows) * 100
