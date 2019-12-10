# Advent of Code 2019: https://adventofcode.com/2019/day/10
# 
# 

import math

class AsteroidMap():

    asteroids = []
    astDict = {}
    count = 0
    width = None
    height = None

    def __init__(self):
        self.count = 0
        self.width = None

    def ReadMap(self, data):
        self.height = len(data)
        for y in range(self.height):
            x = 0
            l = data[y]
            lst = [a for a in l]
            self.width = len(lst) if self.width == None else self.width
            for a in lst:
                if a != '.':
                    self.asteroids.append({'c':(x,y), 'x':x, 'y':y, 'sees':0, 'v':a})
                    self.count += 1
                x += 1
        self.UpdateAsteroidLOS()
        self.ConvertAsteroidListToDict(self.asteroids, self.astDict)

    def UpdateAsteroidLOS(self):
        for i in range(len(self.asteroids)):
            a = self.asteroids[i]
            for n in range(i+1, len(self.asteroids)):
                b = self.asteroids[n]
                if self.IsLineOfSight(a['c'], b['c']):
                    a['sees'] += 1
                    b['sees'] += 1

    def IsLineOfSight(self, a, b):
        posInLOS = self.GetPositionsBetweenAsteroids(a,b)
        for p in posInLOS:
            if p in self.astDict:
                return False

        return True

    def ConvertAsteroidListToDict(self, tup, di): 
        for a in tup: 
            di.setdefault(a['c'], a)
        return di 

    def GetPositionsBetweenAsteroids(self, a, b):
        posBetween = []
        ax, ay = a
        bx, by = b
        rate = (by-ay)/(bx-ax)
        for x in range(ax, bx):
            if rate*x - math.floor(rate*x) < 0.001:
                pos = (x,math.floor(rate*x))
                if pos != a and pos != b:
                    posBetween.append(pos)
        return posBetween

    def GetBestLOS(self):
        return 0

    def RunAgain(self):
        return 0