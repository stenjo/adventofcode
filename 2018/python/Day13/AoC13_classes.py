# Advent of Code 2018: https://adventofcode.com/2018/day/13
#
# Classes

import datetime, time
from datetime import timedelta
import pprint
import collections

class TrackPart():
    x = 0
    y = 0
    orientation = ''
    def __init__(self, x, y, o):
        self.initialize(x, y, o)

    def initialize(self, x, y, o):
        self.x = x
        self.y = y
        self.orientation = o
    
    def print(self):
        return {'x':self.x,'y':self.y,'orientation':self.orientation}



class Track():
    parts = []

    def __init__(self):
        self.parts.clear()

    def addTrackPart(self, trackPart):
        self.parts.append(trackPart)

    def getTrackPart(self, x, y):
        for p in self.parts:
            if p.x == x and p.y == y:
                return p
        return None
    
    def numTrackParts(self):
        return len(self.parts)

    def checkTrackItem(self,t):
        neighbours =  [ self.getTrackPart(t.x+1, t.y),
                        self.getTrackPart(t.x-1, t.y),
                        self.getTrackPart(t.x, t.y+1),
                        self.getTrackPart(t.x, t.y-1)]
        n = 4-neighbours.count(None)
        if (t.orientation == '+' and n == 4) or (t.orientation != '+' and n > 1):
            return True
        return False

    def validateAllTracks(self):
        for t in self.parts:
            if self.checkTrackItem(t) == False:
                return t
        return None
    
    def print(self,carts):
        columns = max([t.x for t in self.parts])+1
        rows = max([t.y for t in self.parts])+1

        for y in range(rows):
            output = ''
            for x in range(columns):
                cart = None
                for c in carts:
                    if c.x == x and c.y == y:
                        cart = c
                if cart != None and cart.crashed == False:
                    output += cart.direction
                else:
                    tp = self.getTrackPart(x,y)
                    if tp != None:
                        output += tp.orientation
                    else:
                        output += ' '
            print(output)




    # def moveCart(self, cart):
    #     trackPart = self.getTrackPart(cart.x, cart.y)
    #     if cart.direction == '^' and trackPart.orientation == '|':
    #         cart.y -= cart.y
    #     return cart


class Cart():
    x = 0
    y = 0
    crashed = False
    direction = ''
    turns = ['L','F','R']
    thisTurn = 0

    def __init__(self, x, y, d):
        self.initialize(x, y, d)

    def initialize(self, x, y, d):
        self.x = x
        self.y = y
        self.direction = d
        self.crashed = False

    def move(self,trackPart):
        self.setNextDirection(trackPart.orientation)
        self.updatePos()

    def updatePos(self):
        if self.direction == '>':
            self.x += 1
        elif self.direction == '^':
            self.y -= 1
        elif self.direction == '<':
            self.x -= 1
        elif self.direction == 'v':
            self.y += 1


    def turn(self):
        m = {'>L':'^','>F':'>','>R':'v','^L':'<','^F':'^','^R':'>','<L':'v','<F':'<','<R':'^', 'vL':'>','vF':'v','vR':'<'}
        c = self.direction + self.turns[self.thisTurn]
        self.thisTurn = (self.thisTurn + 1) % len(self.turns)
        return m[c]
    
    def setNextDirection(self, track):
        # track: |/\-
        if track in ['|','-']:
            return

        if track == '+':
            self.direction = self.turn()
            return

        m = {'^/':'>','>/':'^','</':'v','v/':'<','^\\':'<','<\\':'^','v\\':'>','>\\':'v'}        
        c = self.direction + track
        self.direction = m[c]

    def print(self):
        return '['+str(self.x)+','+str(self.y)+'], dir: '+self.direction


class MineCart():
    carts = []
    track = Track()
    collision = []

    def __init__(self):
        self.carts.clear()
        self.track.parts.clear()

    # Cart handling
    def addCart(self, cart):
        self.carts.append(cart)
    
    def removeCart(self,x,y):
        for c in self.carts:
            if c.x == x and c.y == y:
                self.carts.remove(c)

    def removeCrashed(self):
        for c in self.carts:
            if c.crashed:
                self.carts.remove(c)

    def findCart(self,x,y):
        for c in self.carts:
            if c.x == x and c.y == y:
                return c
        return None
    
    def getCart(self,index):
        if index in range(len(self.carts)):
            return self.carts[index]
        return None
    
    def moveCart(self,i):
        c = self.carts[i]
        tp = self.track.getTrackPart(c.x, c.y)
        c.move(tp)
        if self.hasCollided(c):
            self.collision.append([c.x,c.y])
            c.crashed = True

    def numCarts(self):
        count = 0
        for c in self.carts:
            if c.crashed == False:
                count += 1
        return count

    def loadTracksAndCarts(self, lines):
        self.carts.clear()
        self.track.parts.clear()

        for y in range(len(lines)):
            for x in range(len(lines[y])):
                c = lines[y][x]
                if c in '|-\\/+':
                    self.track.addTrackPart(TrackPart(x,y,c))
                elif c in '<>^v':
                    self.addCart(Cart(x,y,c))
                    if c in '<>':
                        self.track.addTrackPart(TrackPart(x,y,'-'))
                    else:
                        self.track.addTrackPart(TrackPart(x,y,'|'))

    def moveAllOneStep(self):
        for index in range(len(self.carts)):
            self.moveCart(index)

    def moveSteps(self, steps):
        for i in range(steps):
            self.moveAllOneStep()
    
    def hasCollided(self, cart):
        for otherCart in self.carts:
            if cart != otherCart and cart.x == otherCart.x and cart.y == otherCart.y:
                otherCart.crashed = True
                cart.crashed = True
                return True
        return False


    def hasCollision(self):
        return len(self.collision) > 0

    def findCartNotCollided(self):
        result = []
        for c in self.carts:
            if c.crashed == False:
                result.append(c)
        return result

    def findFirstCollision(self):
        self.collision.clear()
        while self.hasCollision() == False:
            self.moveAllOneStep()
        return self.collision

    def findLastCart(self):
        # print(self.track.print(self.carts))
        while self.numCarts() > 1:
            self.moveAllOneStep()
            self.removeCrashed()
            # print(self.track.print(self.carts))
            # print('Remaining carts:',self.numCarts())
        
        return self.findCartNotCollided()[0]