# Advent of Code 2018: https://adventofcode.com/2018/day/10
# 
# 
# import datetime, time
# from datetime import timedelta
import pprint, re

class Point():
    x = 0
    y = 0
    vx = 0
    vy = 0
    def __init__(self, ptArr):
        self.x  = ptArr[0][0]
        self.vx = ptArr[1][0]
        self.y  = ptArr[0][1]
        self.vy = ptArr[1][1]

    def c(self):
        return [self.x,self.y]

    def v(self):
        return [self.vx, self.vy]
    
    # def dump(self):
    #     pp.pprint(self.getArr())

    def getArr(self):
        return [self.c(),self.v()]

    def manhattan(self, pt):
        return abs(self.x-pt.x)+abs(self.y - pt.y)

    def moveOneSecond(self):
        self.x += self.vx
        self.y += self.vy
        return self
    
    def moveMinusOneSecond(self):
        self.x -= self.vx
        self.y -= self.vy
        return self

    def equals(self,p):
        return self.c() == p.c() and self.v() == p.v()
    

class SkyMap():
    Map = []
    MaxX = 0
    MinX = 0
    MaxY = 0
    MinY = 0
    Seconds = 0
    def getlines(self,data):
        for d in data:
            parts = re.split('<|>',d)
            p = Point([[int(s.strip()) for s in parts[1].split(',')], [int(s.strip()) for s in parts[3].split(',')]])
            self.Map.append(p)
            self.updateMaxMin(p)

    def updateMaxMin(self,p):
        if p.x > self.MaxX:
            self.MaxX = p.x
        if p.y > self.MaxY:
            self.MaxY = p.y
        if p.x < self.MinX:
            self.MinX = p.x
        if p.y < self.MinY:
            self.MinY = p.y

    def clearMaxMin(self):
        x = self.MaxX
        self.MaxX = self.MinX
        self.MinX = x
        y = self.MaxY
        self.MaxY = self.MinY
        self.MinY = y

    def append(self,data):
        for d in data:
            self.Map.append(Point(d))

    def load(self,data):
        for p in data:
            self.Map.append(Point([ [ p[0][0], p[0][1] ], [ p[1][0], p[1][1] ] ]))

    def dump(self):
        # pp.pprint(self.map[0].getArr())
        return [p.getArr() for p in self.Map]
    
    def moveOneSecond(self):
        for p in self.Map:
            p.moveOneSecond()
        self.Seconds += 1
        return map
    
    def moveMinusOneSecond(self):
        self.clearMaxMin()
        for p in self.Map:
            p.moveMinusOneSecond()
            self.updateMaxMin(p)
        self.Seconds -= 1
        return map
    
    def getManhattanOfList(self):
        sum = 0
        # cp = self.Map[:]
        for p in self.Map:
            for q in self.Map:
                # print(q)
                sum += p.manhattan(q)
        return sum
    
    def dispose(self):
        self.Map.clear()

    def play(self):
        mhSaved = self.getManhattanOfList()
        while True:
            self.moveOneSecond()
            mh = self.getManhattanOfList()
            # print(mh)
            # if self.Seconds > 2:
            #     break
            if mhSaved > mh:
                mhSaved = mh
            else:
                self.moveMinusOneSecond()
                return mhSaved

    def hasPoint(self,x,y):
        for p in self.Map:
            if p.x == x and p.y == y:
                return True
        return False


    def plot(self):
        string = ''
        print('X:',self.MinX-1,'-',self.MaxX+2)
        print('Y:',self.MinY-1,'-',self.MaxY+2)
        print('Time:',self.Seconds)

        for y in range(self.MinY-1, self.MaxY+2):
            for x in range(self.MinX-1, self.MaxX+2):
                if self.hasPoint(x,y):
                    string += '#'
                else:
                    string += '.'
            print(string)
            # outData.write(string+'\n')
            string = ''

    # def __init__(self):
    #     self.m = []
