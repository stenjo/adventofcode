import re

class Schematic:
    def __init__(self,schema):
        self.schema = schema
        
    def partNumbers(self, lines):
        nums = []
        for lineNo in range(len(lines)):
            start = None
            for idx in range(len(lines[lineNo])):
                if lines[lineNo][idx].isdigit() == False:
                    if start != None and self.checkForSymbols(lines, lineNo, start, idx):
                        nums.append(int(lines[lineNo][start:idx]))
                    start = None
                else:
                    if start == None:
                        start = idx
            if start != None and self.checkForSymbols(lines, lineNo, start, idx):
                nums.append(int(lines[lineNo][start:len(lines[lineNo])]))
            
        return nums
    
    def hasSymbol(self, lines, lineNo, start, end):
        if lineNo < 0: return False
        if lineNo >= len(lines): return False
            
        if start > 0: start -= 1
        if end < len(lines[lineNo]): end += 1
        
        if re.search("^[\d\.]*$", lines[lineNo][start:end]):
            return False
        
        return True
    
    def checkForSymbols(self, lines, lineNo, start, end):
        
        for l in range( lineNo -1, lineNo+ 2):
            if self.hasSymbol(lines, l, start, end):
                return True
            