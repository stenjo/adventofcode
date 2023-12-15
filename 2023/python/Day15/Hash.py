
import re


class Hash:
    def __init__(self, input):
        self.hashStrings = [s.strip() for s in input.split(',')]
        
    def hash(self, string=None):
        string = self.hashStrings[0] if string is None else string
        val = 0
        for c in string:
            val += ord(c)
            val *= 17
            val %= 256
            
        return val
    
    def sumOfHashes(self):
        return sum([self.hash(s) for s in self.hashStrings])
    
    def sumOfFocusingPower(self):
        boxes = [[] for _ in range(256)]
        self.adjustLenses(boxes)
        
        return self.focusPowerSum(boxes)

    def adjustLenses(self, boxes):
        for c in self.hashStrings:
            op = '=' if '=' in c else '-'
            label, value = re.split('=|-', c)
            boxNo = self.hash(label)
            
            if op == '=':
                index = self.indexOfLens(boxes, boxNo, label)
                if index != None:
                    boxes[boxNo].remove(boxes[boxNo][index])
                    boxes[boxNo].insert(index, (label, int(value)))
                else:
                    boxes[boxNo].append((label, int(value)))
            else:
                self.removeLens(boxes, label, boxNo)
               

    def focusPowerSum(self, boxes):
        fp = 0
        for i, box in enumerate(boxes):
            for j, lens in enumerate(box):
                fp += (i+1)*(j+1)*lens[1]
        return fp

    def indexOfLens(self, boxes, boxNo, label):
        found = [ i for i,l in enumerate(boxes[boxNo]) if l[0] == label]
        if len(found) > 0:
            return found[0]
        return None

    def removeLens(self, boxes, label, boxNo):
        lenses = boxes[boxNo]
        found = [ l for l in lenses if l[0] == label]
        if len(found) == 1:
            boxes[boxNo].remove(found[0])