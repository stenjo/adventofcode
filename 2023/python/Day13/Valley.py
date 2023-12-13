
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
        mirrorLines=[[i for i in range(len(line)) if self.isMirror(line,i)] for line in notes]
        return list(set.intersection(*map(set,mirrorLines)))
    
    def findMirrorRow(self):
        t = list(map(list, zip(*self.map)))
        r = list(map(list, zip(*t)))
        
        lines = self.findMirror(r)
        return lines[-1] if len(lines) > 0 else 0

    def findMirrorCol(self):
        t = list(map(list, zip(*self.map)))
        lines = self.findMirror(t)
        return lines[-1] if len(lines) > 0 else 0
        
    def isMirror(self, line, p):
        mRange = min([len(line) - p, p])
        return line[p-mRange:p] == line[p:p+mRange][::-1]
        