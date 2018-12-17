# Advent of Code 2018: https://adventofcode.com/2018/day/17
#
# Classes

import datetime, time
from datetime import timedelta
import pprint
import collections

class Unit():
    _dead = False
    def __init__(self,x,y):
        self._x = x
        self._y = y
        self._hitpoints = 200
        self._attackPower = 3
        self._dead == False
        self._name = 'None'
    
    # Properties
    #

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def hitpoints(self):
        return self._hitpoints

    @hitpoints.setter
    def set_hitpoints(self, value):
        self._hitpoints = value
        if self._hitpoints <= 0:
            self._dead = True

    @property
    def name(self):
        return self._name

    def IsDead(self):
        return self._dead

    def move(self, dir):
            self._y += dir.y
            self._x += dir.x
    
    def fight(self, unit):
        unit.hitpoints -= self._attackPower

    def position(self):
        return [self._x, self._y]


class Goblin(Unit):
    def __init__(self,x,y):
        Unit.__init__(self,x,y)
        self._name = 'Goblin'

class Elf(Unit):
    def __init__(self,x,y):
        Unit.__init__(self,x,y)
        self._name = 'Elf'

class Wall:
    def __init__(self,x,y):
        self._x = x
        self._y = y
    
    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

class Direction:
    def __init__(self,x,y):
        self._x = x
        self._y = y
    
    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y
    def a(self):
        return [self._x, self._y]


class WaterFountain:

    def __init__(self):
        self._grid = [[]]
        self._maxX = 0
        self._minX = 1000000
        self._maxY = 0

    def load(self,data):
        for line in data:
            parts = line.split(',')
            if parts[0].split('=')[0].lower() == 'x':
                xRange = parts[0].split('=')[1].strip().replace('..',':')
                # print('xRange:',xRange)
                yRange = parts[1].split('=')[1].strip().replace('..',':')
                
            elif parts[0].split('=')[0].lower() == 'y':
                yRange = parts[0].split('=')[1].strip().replace('..',':')
                # print('yRange:',yRange)
                xRange = parts[1].split('=')[1].strip().replace('..',':')
            
            if ':' not in xRange: xRange += ':'+str(int(xRange))
            if ':' not in yRange: yRange += ':'+str(int(yRange))

            yFrom = int(yRange.split(':')[0].strip())
            yTo = int(yRange.split(':')[1].strip())
            # print('yRange:',yRange, 'yFrom:', yFrom, 'yTo:', yTo)

            xFrom = int(xRange.split(':')[0].strip())
            xTo = int(xRange.split(':')[1].strip())
            # print('xRange:',xRange)

            for y in range(yFrom, yTo + 1):
                if self._maxY < y: self._maxY = y 
                for x in range(xFrom, xTo + 1):
                    if self._maxX < x: self._maxX = x 
                    if self._minX > x: self._minX = x 
                    self.putGridItem('#',x,y)

        # for y in range(len(data)):
        #     l = data[y]
        #     for x in range(len(l)):
        #         c = data[y][x]
        #         if c == '#':
        #             self._walls.append(Wall(x,y))
        #             self.putGridItem(c,x,y)
        #         elif c == 'G':
        #             self._goblins.append(Goblin(x,y))
        #         elif c == 'E':
        #             self._elfs.append(Elf(x,y))
    
    def numGoblins(self):
        return len(self._goblins)

    def numElfs(self):
        return len(self._elfs)

    def getUnitAt(self, x, y):
        for u in self._elfs:
            # print('Elfs:',u.x, x, u.y, y)
            if u.x == x and u.y == y:
                return u
        for u in self._goblins:
            # print('Goblins:',u.x, x, u.y, y)
            if u.x == x and u.y == y:
                return u
        return None

    def putGridItem(self,t,x,y):

        while len(self._grid) <= y and y > 0:
            self._grid.append([])
   
        while len(self._grid[y]) <= x and x > 0:
            self._grid[y].append('.')

        if len(self._grid[y]) == 0:
            self._grid[y].append(t)
        elif x in range(len(self._grid[y])) and len(self._grid[y]) > 0:
            self._grid[y][x] = t
        else:
            self._grid[y].append(t)

    def getGridItem(self, x, y):
        if y+1 > len(self._grid): return None
        if x+1 > len(self._grid[y]): return None
        item = self._grid[y][x]
        if item == None or item == '.': return None
        return item

    def isWall(self, x, y):
        if self._grid[y][x] == '#':
            return True
        return False

    def findWalls(self, x,y):
        rightWall = None
        leftWall = None
        for col in range(x,self._maxX+1):
            print(col,y)
            if self.getGridItem(col, y) == '#':
                rightWall = col 
            break

        for col in range(x,-self._minX-1):
            print(col,y)
            if self.getGridItem(col, y) == '#':
                leftWall = col 
            break
            
        return [leftWall,rightWall]
    
    def findEdge(self, x,y):
        for col in range(x,self._maxX+1):
            if self.getGridItem(col, y+1) == None:
                rightEdge = col 
                break
        for col in range(x,-self._minX-1):
            if self.getGridItem(col, y+1) == None:
                leftEdge = col
                break

        return [leftEdge,rightEdge]

    def isOverflowing(self, x,y):
        return False

    def fillWaterOnLine(self, x, y):
        walls = self.findWalls(x,y)
        leftWall = walls[0]
        rightWall = walls[1]
        if leftWall == None or rightWall == None: return
        for col in range(walls[0],walls[1]):
            self.putGridItem('~',col,y)

    def printGrid(self):
        # print header
        print()
        s = '   '
        for x in range(self._minX-1, self._maxX+1): s += str(int(x/100))
        print(s)
        s = '   '
        for x in range(self._minX-1, self._maxX+1): s += str(int((x%100)/10))
        print(s)
        s = '   '
        for x in range(self._minX-1, self._maxX+1): s += str(int(x%10))
        print(s)

        for y in range(self._maxY+2):
            s = ''
            for x in range(self._minX-1, self._maxX+2):
                if y == 0 and x == 500: s += '+'
                else:
                    item = self.getGridItem(x,y)
                    if item == None:
                        s += ' '
                    else:
                        s += item
            print('{0:2d} {1:s}'.format(y,s))

    def doFillWithWater(self):
        x = 500
        for y in range(self._maxY):
            if self.getGridItem(x,y) == None:
                self.putGridItem('|',x,y)
            elif self.getGridItem(x,y) == '#':
                self.fillWaterOnLine(x,y-1)
                if self.isOverflowing(x,y-1):
                    x = self.findEdge(x,y-1)
                break    


    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, i):
        self._index = i%len(i)

    def getScores(self):
        return 0


