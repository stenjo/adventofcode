
class SourceDestination:
    def __init__(self,input = ""):
        self.input = input
        self.itemsMap = {}
        if len(input.strip()) == 0: return
        
        self.parseInput(input)

    def parseInput(self, input):
        dest, source, count = [int(n) for n in input.split(' ') if n != '']
        for n in range(count):
            self.itemsMap[source+n] = dest + n
                    
    def items(self):
        return self.itemsMap
    
    def getMapped(self, source):
        if source in self.itemsMap.keys():
            return self.itemsMap[source]

        return source