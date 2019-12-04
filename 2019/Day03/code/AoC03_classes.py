# Advent of Code 2019: https://adventofcode.com/2019/day/3
# 
# 
import math
from pprint import pprint

class WireLine():

    b = {}
    intersections = []
    x = 0
    y = 0
    series = 0

    def __init__(self):
        super().__init__()

    def GetMoveCoordinates(self, x, y, move):
        coords = []
        mDir = move[0]
        mSteps = move[1]
        incr = 1
        if mDir in ['L','D']:
            incr = -1
        
        if mDir in ['R','L']:   # Move horizontally - change x
            start = x + incr
            end = x + incr * mSteps + incr
            for n in range(start, end, incr):
                coords.append((n, y))
        else:
            start = y + incr
            end = y + incr * mSteps + incr
            for n in range(start, end, incr):
                coords.append((x, n))

        return coords

    def AddWireline(self, linemap):
        self.series += 1
        moveList = self.CreateMoveList(linemap)
        cPos = (0,0)
        steps = 0
        for move in moveList:
            cList = self.GetMoveCoordinates(cPos[0], cPos[1], move)
            for c in cList:
                cPos = c
                steps += 1
                if c in self.b:
                    if self.b[c][0] != self.series:
                        (x,y) = c
                        self.intersections.append([x,y, steps+self.b[c][1]])
                else:
                    self.b[c]=(self.series,steps)
    
    def GetMove(self, pathItem):
        direction = pathItem[0]
        pathItem = str.replace(pathItem, direction, '0')
        length = int(pathItem)
        moveItem = [direction,length]
        return moveItem
        
    def CreateMoveList(self, items):
        mList = []
        r = range(len(items))
        for i in range(0,len(items)):
            mList.append(self.GetMove(items[i]))

        return mList 

    def Manhattan(self, coord):
        return abs(coord[0]) + abs(coord[1])
        # return abs(int(coord[0]-int(self.columns/2))) + abs(int(coord[1])-int(self.rows/2))

    def FindClosest(self):
        distance = self.Manhattan(self.intersections[0])
        for c in self.intersections[1:]:
            if self.Manhattan(c) < distance:
                distance = self.Manhattan(c)
        return distance


    def FindFewerSteps(self):
        self.intersections.sort(key=lambda c: c[2])
        pprint(self.intersections, depth=2, width=18)
        return self.intersections[0][2]