import re

class Schematic:
    def __init__(self,schema):
        self.schema = schema
        self.starMap = {}
        
    def partNumbers(self, lines= None):
        if lines == [] or lines == None:
            lines = self.schema
        nums = []
        for lineNo in range(len(lines)):
            start = None
            for idx in range(len(lines[lineNo])):
                if lines[lineNo][idx].isdigit() == False:
                    self.addNums(lines, nums, lineNo, start, idx)
                    start = None
                else:
                    if start == None:
                        start = idx
            self.addNums(lines, nums, lineNo, start, len(lines[lineNo]))
            
        return nums

    def addNums(self, lines, nums, lineNo, start, idx):
        if start != None and self.checkForSymbols(lines, lineNo, start, idx):
            number = int(lines[lineNo][start:idx])
            nums.append(number)
            for star in self.hasAdjacentStar(lines, lineNo, start, idx):
                if star not in self.starMap.keys():
                    self.starMap[star]= [number]
                else:
                    self.starMap[star].append(number)
    
    def hasSymbol(self, lines, lineNo, start, end):
        if lineNo < 0: return False
        if lineNo >= len(lines): return False
            
        if start > 0: start -= 1
        if end < len(lines[lineNo]): end += 1
        
        if re.search("^[\d\.]*$", lines[lineNo][start:end]):
            return False
        
        return True

    def getStarIndexes(self, line):
        return [i for i, letter in enumerate(line) if letter == '*']


    def hasStar(self, lines, lineNo, start, end):
        if lineNo < 0: return []
        if lineNo >= len(lines): return []
            
        if start > 0: start -= 1
        if end < len(lines[lineNo]): end += 1
        
        stars = []
        starIndexes = self.getStarIndexes(lines[lineNo][start:end:])
        if starIndexes != []:
            for p in starIndexes:
                stars.append((lineNo,p+start))
            return stars
        
        return []
    
    def checkForSymbols(self, lines, lineNo, start, end):
        
        for l in range( lineNo -1, lineNo+ 2):
            if self.hasSymbol(lines, l, start, end):
                return True
            
    def hasAdjacentStar(self, lines, lineNo, start, end):
        stars = []
        for l in range( lineNo -1, lineNo+ 2):
            stars += self.hasStar(lines, l, start, end)
        return stars
    
    def getGearRatioSum(self):
        sum = 0
        for nums in self.starMap.values():
            if len(nums) == 2:
                sum += nums[0]*nums[1]
        return sum