
class StarMap:
    def __init__(self, input):
        self.stars = []
        self.stars = [list(l.strip()) for l in input]
        self.expand()
        
        
    def expand(self):
        self.emptyRows = [y for y,r in enumerate(self.stars) if '#' not in r]
        t = list(map(list, zip(*self.stars)))
        self.emptyColumns = [x for x,c in enumerate(t) if '#' not in c]
        
    def sumOfGalaxyDistances(self):
        galaxies = []
        for y,line in enumerate(self.stars):
            for x,c in enumerate(line):
                if '#' == c:
                    galaxies.append((x,y))

        distances = []
        for i, galaxy in enumerate(galaxies):
            distances += [self.manhattanDistance(galaxy, g) for start, g in enumerate(galaxies) if start > i]
        
        return sum(distances)
    
    def manhattanDistance(self, a, b, multiplier=1):
        multiplier = multiplier - 1 if multiplier > 1 else 1
        cols = range(a[0]+1, b[0]) if b[0] > a[0] else range(b[0]+1, a[0]) 
        addX = len(set(cols).intersection(self.emptyColumns)) * multiplier
        rows = range(a[1]+1, b[1]) if b[1] > a[1] else range(b[1]+1, a[1])
        addY = len(set(rows).intersection(self.emptyRows)) * multiplier
        
        return abs(b[0]-a[0])+addX + abs(b[1]-a[1])+addY
        
    def sumOfGalaxyLargeDistances(self, multiplier):
        return sum(self.getGalaxyPairs(multiplier).values())

    def getGalaxies(self):
        galaxies = []
        for y,line in enumerate(self.stars):
            for x,c in enumerate(line):
                if '#' == c:
                    galaxies.append((x,y))
        return galaxies
        
    def getGalaxyPairs(self, mul=1):
        galaxies = self.getGalaxies()
        pairs = {}
        for i, galaxy in enumerate(galaxies):
            for start, g in enumerate(galaxies):
                if start > i:
                    pairs[(galaxy, g)] = self.manhattanDistance(galaxy,g, mul)
        
        return pairs
        