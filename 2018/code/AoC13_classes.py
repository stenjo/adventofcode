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


class Track():
    parts = []

    def addTrackPart(self, trackPart):
        self.parts.append(trackPart)

    def getTrackPart(self, x, y)
        for i in range(len(parts)):
            if parts[i].x == x and parts[i].y == y
                return parts[i]
    
    def moveCart(self, cart):
        trackPart = self.getTrackPart(cart.x, cart.y)
        if cart.direction == '^' and trackPart.orientation == '|':
            cart.y -= cart.y
        return cart


class Cart():
    x = 0
    y = 0
    direction = ''

    def __init__(self, x, y, d):
        self.initialize(x, y, d)

    def initialize(self, x, y, d):
        self.x = x
        self.y = y
        self.direction = d


class MineCart():
    def addCart(self):
        return

    def runSim(self):
        return 0