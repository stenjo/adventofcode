# Advent of Code 2019: https://adventofcode.com/2019/day/10
# 
# 

import math
from matplotlib import pylab as pt, pyplot as plt
import numpy as np

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
            l = data[y].strip()
            lst = [a for a in l]
            self.width = len(lst) if self.width == None else self.width
            for a in lst:
                if a != '.':
                    self.asteroids.append({'c':(x,y), 'x':x, 'y':y, 'sees':0, 'v':a})
                    self.count += 1
                x += 1
        self.ConvertAsteroidListToDict(self.asteroids, self.astDict)
        self.UpdateAsteroidLOS()

    def UpdateAsteroidLOS(self):
        for i in range(len(self.asteroids)):
            a = self.asteroids[i]
            for n in range(i+1, len(self.asteroids)):
                b = self.asteroids[n]
                los = self.IsLineOfSight(a['c'], b['c'])
                if  los == True:
                    a['sees'] += 1
                    b['sees'] += 1
                # print(i,n, los)

    def IsLineOfSight(self, a, b):
        # posInLOS = self.GetPositionsBetweenAsteroids(a,b)
        # for p in posInLOS:
        #     if p in self.astDict:
        #         return False
        for n in [d['c'] for d in a.asteroids]:
            if self.IsLineOfSight(a,b,n):
                return False

        return True

    def ConvertAsteroidListToDict(self, tup, di): 
        for a in tup: 
            di.setdefault(a['c'], a)
        return di 

    def IsInLineOfSight(self, a, b, m):
        if self.LessThan(a,b):
            ax, ay = a
            bx, by = b
        else:
            ax, ay = b
            bx, by = a

        mx, my = m

        if a == b or a == m or b == m: return False

        if  bx - ax == 0:   # vertical line of sight
            if mx == ax and my in range(ay, by, 1 if ay < by else -1)
                return True
            else:
                return False
        else:
            k = (ay-by)/(ax-bx)
            c = ay-k*ax
            y = k*mx+c
            if mx in range(ax,bx) 
                and my in range(ay, by, 1 if ay < by else -1)
                and my == int(y)
                and y.is_integer():
                return True
            
        return False

    def LessThan(self, a, b):
        if a[0] > b[0] or (a[0] == b[0] and a[1] > b[1]):
            return False
        else:
            return True

    def GetPositionsBetweenAsteroids(self, a, b):
        posBetween = []
        if a == b: return posBetween

        if a[0] > b[0] or (a[0] == b[0] and a[1] > b[1]):
            ax, ay = b
            bx, by = a
        else:
            ax, ay = a
            bx, by = b

        # y = kx + c
        # k = (y - c)/x
        # c = y - kx
        # ay - kax = by - kbx
        # ay - by = kax - kbx
        # k = (ay-by)/(ax-bx)

        if  bx - ax == 0:   # horizontal line of sight
            posBetween = [(ax, n) for n in range(ay+1, by)]
        # elif by - ay == 0:  # vertical line of sight
        #     posBetween = [(n, ay) for n in range(ax+1, bx)]
        else:
            k = (ay-by)/(ax-bx)
            c = ay-k*ax
            for x in range(ax, bx):
                y = k*x + c
                if y.is_integer():
                    p = (x, int(y))
                    posBetween.append(p)
                    # if p == (11,13):
                        # print('k:',k, ' c:',c, ' x:', x, ' y:',int(y))

        if a in posBetween: posBetween.remove(a) 
        if b in posBetween: posBetween.remove(b)

        return posBetween

    def PrintAsteroids(self):
        for y in range(self.height):
            line = ''
            for x in range(self.width):
                if (x,y) in self.astDict:
                    if (x,y) == self.GetBestLOS():
                        line += '('+str(self.astDict[(x,y)]['sees']).rjust(3,' ')+')'
                    else:
                        line += str(self.astDict[(x,y)]['sees']).rjust(4,' ')+' '
                else:
                    line += '  .  '

            print(line)

    def PlotAsteroids(self):
        data = {
            'x': [d['x'] for d in self.asteroids],
            'y': [d['y'] for d in self.asteroids]
        }
        plt.scatter('x','y', data=data)
        # plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'bo')
        plt.axis([-1, self.width, self.height, -1])
        plt.show()

    def GetBestLOS(self):
        res = list(sorted(self.asteroids, key=lambda a: a['sees']))
        res.reverse()
        return res[0]['c']

    def RunAgain(self):
        return 0