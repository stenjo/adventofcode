# Advent of Code 2019: https://adventofcode.com/2019/day/8
# 
# 
import math

class Mapper():

    mapData = []
    width = 0
    height = 0
    image = []
    layers = []

    def __init__(self, data, size):
        self.width, self.height = list(map(int, size.split('x')))
        self.LoadRawMap(data)
        self.SplitRawToImage()

    def LoadRawMap(self, data):
        self.mapData = list(map(int, data))

    def SplitRawToImage(self):
        n = self.width * self.height
        self.layers = [self.mapData[i:i + n] for i in range(0, len(self.mapData), n)]

    def GetPixelAt(self, point):
        pixel = ' '
        for layer in range(len(self.layers))[::-1]:
            val = self.layers[layer][point]
            if  val == 0:
                pixel = ' '
            elif val == 1:
                pixel = '*'

        return pixel


    def LowestZeros(self):
        result = {'layer':None, 'zeros':0}
        for n in range(len(self.layers)):
            numZeros = self.layers[n].count(0)
            if result['layer'] == None or result['zeros'] > numZeros:
                result = {'layer':n, 'zeros':numZeros}

        return result

    def GetOneByTwos(self, layer):
        layer = self.layers[layer-1]
        ones = layer.count(1)
        twos = layer.count(2)

        return ones*twos

    def Find1x2OnLowest0(self):
        l = self.LowestZeros()

        return self.GetOneByTwos(l['layer']+1)
    
    def PrintImage(self):
        for y in range(self.height):
            line = ''
            for x in range(self.width):
                line += self.GetPixelAt(y*self.width + x)
            print(line)



