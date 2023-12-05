class SourceDestination:
    def __init__(self, input=""):
        self.input = input
        # self.itemsMap = {}
        self.mapping = {}
        if len(input.strip()) == 0:
            return

        self.parseInput(input)

    def parseInput(self, input):
        dest, source, count = [int(n) for n in input.split(" ") if n != ""]
        # for n in range(count):
        #     self.itemsMap[source + n] = dest + n
        self.mapping[source] = (dest, count)

    def getMapped(self, source):
        for s, (d, c) in self.mapping.items():
            if source >= s and source < s + c:
                return source - s + d
        return source
