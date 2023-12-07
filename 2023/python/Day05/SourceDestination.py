class SourceDestination:
    def __init__(self, input=""):
        self.input = input
        self.mapping = {}
        if len(input.strip()) == 0:
            return

        self.parseInput(input)

    def parseInput(self, input):
        dest, source, count = [int(n) for n in input.split(" ") if n != ""]
        self.mapping[source] = (dest, count)

    def getMapped(self, source):
        for s, (d, c) in self.mapping.items():
            if source >= s and source < s + c:
                return source - s + d
        return source

    def getDestRange(self):
        r = []
        for source, (dest, count) in self.mapping.items():
            r+=list(range(dest, dest + count))

        r.sort()
        
        return r

    def getSource(self, dest):
        for s, (d, c) in self.mapping.items():
            if dest >= d and dest < d + c:
                return dest - d + s
        return dest
