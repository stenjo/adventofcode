
from collections import Counter, defaultdict
from itertools import zip_longest


class Valley:
    def __init__(self, input):
        self.patterns = []
        pattern = []
        for line in input:
            if len(line.strip()) > 0:
                pattern.append(line.strip())
            else:
                self.patterns.append(pattern)
                pattern = []
        if len(pattern):
            self.patterns.append(pattern)
            
    def rowsByColumnsSum(self):
        rows = [Pattern(r).findMirrorRow() for r in self.patterns]
        cols = [Pattern(c).findMirrorCol() for c in self.patterns]
        return sum(rows) + sum(cols)*100
        

class Pattern:
    def __init__(self,input):
        self.map = [line.strip() for line in input]
        
    def findMirror(self, notes):
        mirrorLines = self.findMirrorLines(notes)
        return list(set.intersection(*map(set,mirrorLines)))

    def findMirrorLines(self, notes = None, transpose=False):
        if notes is None: notes = self.map
        t = list(map(list, zip(*notes))) if transpose else notes
        mirrorLines=[[i for i in range(len(line)) if self.isMirror(line,i) and i > 0] for line in t]
        return mirrorLines
    
    def findMirrorRow(self):
        lines = self.findMirror(self.map)
        return lines[-1] if len(lines) > 0 else 0

    def findMirrorCol(self):
        t = list(map(list, zip(*self.map)))
        lines = self.findMirror(t)
        return lines[-1] if len(lines) > 0 else 0
        
    def isMirror(self, line, p):
        mRange = min([len(line) - p, p])
        return line[p-mRange:p] == line[p:p+mRange][::-1]
    
    def findSmudgedPixel(self, notes):
        ml = self.findMirrorLines(notes)
        counts = defaultdict(int)
        for i,l in enumerate(ml):
            if i in l: counts[i] += 1
            
        other = list(map(list, zip_longest(*ml, fillvalue=None)))
        options = map(tuple, other)
        
        return True