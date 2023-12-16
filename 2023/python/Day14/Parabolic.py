
class Parabolic:
    def __init__(self,input=[]):
        self.dishMap = [list(l.strip()) for l in input]
        self.tiltedMap = []

    def boulderDist(self, x,y):
        return len(self.dishMap) - y
    
    def rolledNorth(self):
        # get col count of boulders
        c = list(map(list, zip(*self.dishMap)))
        ranges = []
        length = len(self.dishMap[0])
        rowMap = []
        for i,l in enumerate(c):
            ranges.append(0)
            parts = "".join(l).split('#')
            pos = 0
            row = []
            for part in parts:
                cnt = part.count('O')
                ranges[i] += sum(range(length-pos, length-pos - cnt, -1))
                pos += len(part) + 1
                row.append(self.createPart(cnt, len(part)))
            rowMap.append("#".join(row))
            
        # self.tiltedMap = rowMap                
        self.tiltedMap = self.rotate(rowMap)                
        return ranges
    
    def tilted(self, notes):
        l = len(notes[0])
        tilted = ['O']*4+['.']*1+['#']+['.']*2
        return tilted
    
    def createPart(self, boulders, length):
        return "".join(['O']*boulders + ['.']*(length-boulders))
    
    def printMap(self, notes):
        for n in notes:
            print(n)
            
    def rotate(self, notes):
        return list(map(str, zip(notes)))