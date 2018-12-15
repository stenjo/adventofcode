# Advent of Code 2018: https://adventofcode.com/2018/day/15
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

    def IsDead(self):
        return self._dead

    def move(self, dir):
        if dir == 'up':
            self._y -=1
        elif dir == 'left':    
            self._x +=1
        elif dir == 'down':    
            self._y +=1
        elif dir == 'right':    
            self._x -=1
    
    def fight(self, unit):
        unit.hitpoints -= self._attackPower

    def position(self):
        return [self._x, self._y]


class Goblin(Unit):
    def name(self):
        return 'Goblin'

class Elf(Unit):
    def name(self):
        return 'Elf'

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


class BeverageBandidts:

    def __init__(self):
        self._grid = [[]]
        self._elfs = []
        self._goblins = []
        self._walls = []

    def load(self,data):
        for y in range(len(data)):
            l = data[y]
            for x in range(len(l)):
                c = data[y][x]
                if c == '#':
                    self._walls.append(Wall(x,y))
                elif c == 'G':
                    self._goblins.append(Goblin(x,y))
                elif c == 'E':
                    self._elfs.append(Elf(x,y))
                self.putGridItem(c,x,y)
    
    def numGoblins(self):
        return len(self._goblins)

    def numElfs(self):
        return len(self._elfs)

    def getUnitAt(self, x, y):
        for u in self._elfs:
            if u.x == x and u.y == y:
                return u
        for u in self._goblins:
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

        return [x,y]
    
    def getNearest(self, source):
        if source.name() == 'Elf':
            return self._getNearest(source, self._goblins)
        elif source.name() == 'Goblin':
            return self._getNearest(source, self._elfs)


    def _getNearest(self, unit, _list):
        closer = 1000000
        nearest = None
        for u in _list:
            distance  = self.distanceTo(unit,u)
            if distance < closer or (u == closer and (u.y < nearest.y or (u.y < nearest.y and u.x < nearest.x))):
                closer = distance
                nearest = u
        return unit


    def printGrid(self):
        print()
        for y in range(len(self._grid)):
            s = ''
            for x in range(len(self._grid[y])):
                s += self._grid[y][x]
            print(s)

            
    @property
    def index(self):
        return self._index

    @index.setter
    def index(self, i):
        self._index = i%len(i)

    def getScores(self):
        return 0


