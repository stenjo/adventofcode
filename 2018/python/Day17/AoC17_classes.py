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

class Width:
    def __init__(self,l,r):
        self._left = l
        self._right = r
    
    @property
    def left(self):
        return self._left
    
    @left.setter
    def left(self,v):
        self._left = v

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, v):
        self._right = v

    @property
    def a(self):
        return [self._left, self._right]

    @property
    def r(self):
        return list(range(self._left+1, self._right))

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
        if self.getGridItem(x, y) == '#':
            return True
        return False

    def findWalls(self, x,y):
        w = Width(0,0)
        for column in range(x,self._maxX+2):
            if self.isWall(column, y):
                w.right = column 
                break

        for column in range(x,self._minX-1,-1):
            if self.isWall(column, y):
                w.left = column 
                break
            
        return w
    
    def findEdge(self, x,y):
        edges = Width(0,0)
        for col in range(x+1,self._maxX+1):
            if self.getGridItem(col, y+1) == None:
                edges.right = col 
                break

        for col in range(x-1,self._minX-1,-1):
            if self.getGridItem(col, y+1) == None:
                edges.left = col
                break

        return edges

    def isOverflowing(self, x,y):
        return False

    def fillWaterOnLine(self, x, y):
        walls = self.findWalls(x,y)
        if walls.left == None or walls.right == None: 
            return walls
        for col in walls.r:
            self.putGridItem('~',col,y)

        return walls

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
                y -=1
                self.fillWaterOnLine(x,y-1)
                y -=1
                self.fillWaterOnLine(x,y-1)
                y -=1
                self.fillWaterOnLine(x,y-1)
                    # if self.isOverflowing(x,y-1):
                    #     x = self.findEdge(x,y-1)
                break    

    def tryDown(self, x, y):
        if y > self._maxY : return
        print(x,y)
        if self.isWall(x,y+1):
            width = self.findWalls(x,y)
            for col in width.r:
                if self.getGridItem(x,y) == None:
                    self.putGridItem('|',col,y)
                    self.tryDown(col,y)
            self.fillWaterOnLine(x,y)
        elif self.getGridItem(x,y+1) == None:
            self.putGridItem('|',x,y)
            self.tryDown(x,y+1)
            width = self.findWalls(x,y)
            for col in width.r:
                if self.getGridItem(x,y) == None:
                    self.putGridItem('|',col,y)
                    self.tryDown(col,y)
        self.fillWaterOnLine(x,y)
        edges = self.findEdge(x,y)
        if edges.left != 0:
            print ('left:',x,y,edges.left)
            return
            self.tryDown(edges.left,y)
        if edges.right != 0:
            print('right:',x,y,edges.right)
            return
            self.tryDown(edges.right,y)


    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, i):
        self._index = i%len(i)

    def getScores(self):
        return 0


