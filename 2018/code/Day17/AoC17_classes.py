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
        return self._grid[y][x]

    def isWall(self, x, y):
        if self._grid[y][x] == '#':
            return True
        return False

    def distanceTo(self, source, dest):
        return abs(source.x - dest.x) + abs(source.y-dest.y)
    
    def directionTo(self, source, dest):
        x = (dest.x - source.x)
        if x != 0:
            x = -1 if x < 0 else 1

        y = (dest.y - source.y)
        if y != 0:
            y = -1 if y < 0 else 1

        return Direction(x,y)
    

    def getNearestTo(self, source):
        if source == None:
            return None
        if source.name == 'Elf':
            return self._getNearest(source, self._goblins)
        elif source.name == 'Goblin':
            return self._getNearest(source, self._elfs)

    def _getNearest(self, unit, _list):
        closer = 1000000
        nearest = None
        # print('unit:', unit.x, unit.y, unit.name)
        for u in _list:
            distance  = self.distanceTo(unit,u)
            # print('u:', u.x, u.y, u.name, distance)
            if nearest == None:
                nearest = u
                closer = distance
            elif distance < closer or (u == closer and (u.y < nearest.y or (u.y < nearest.y and u.x < nearest.x))):
                closer = distance
                nearest = u

        # print('unit:', nearest.x, nearest.y, nearest.name, closer)
        return nearest

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
                        s += '.'
                    else:
                        s += item
            print('{0:2d} {1:s}'.format(y,s))

    def doRound(self):
        for y in range(len(self._grid)):
            for x in range(len(self._grid[y])):
                if self.isWall(x,y) == False:
                    unit = self.getUnitAt(x,y)
                    if unit != None:
                        self._round.append(unit)
                        print(unit.name, ':', unit.x, unit.y)
                        
        for unit in self._round:
            nearest = self.getNearestTo(unit)
            dir = self.directionTo(unit, nearest)
            if self.isWall(unit.x+dir.x, unit.y+dir.y) == False:
                unit.move(dir)
                print(unit.name, 'moved by', dir.a(), 'to', unit.x, unit.y)



    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, i):
        self._index = i%len(i)

    def getScores(self):
        return 0


