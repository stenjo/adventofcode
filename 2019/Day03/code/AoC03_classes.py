# Advent of Code 2019: https://adventofcode.com/2019/day/3
# 
# 
import math

class WireLine():

    a = []
    rows = 0
    columns = 0
    intersections = []

    def __init__(self, rows, columns):
        super().__init__()
        self.rows = rows
        self.columns = columns
        # a = [[0] * self.columns for i in range(self.rows)]
        for i in range(self.rows):
            self.a.append(['.'] * self.columns)
        
    def AddWireline(self,linemap):
        # moves = linemap.split(',')
        ox = int(self.rows/2)
        posX = ox
        oy = int(self.columns/2)
        posY = oy
        moveList = self.CreateMoveList(linemap)
        self.a[posX][posY] = 'O'
        for move in moveList:
            if move[0] == 'R':
                for x in range(posX+1, posX+move[1]):
                    if self.a[posY][x] != '.':
                        self.a[posY][x] = 'X'
                        self.intersections.append([posY-oy,x-ox])
                    else:
                        self.a[posY][x] = '-'
                posX += move[1]

            if move[0] == 'U':
                for y in range(posY+1, posY+move[1]):
                    if self.a[y][posX] != '.':
                        self.a[y][posX] = 'X'
                        self.intersections.append([y-oy,posX-ox])
                    else:
                        self.a[y][posX] = '|'
                posY += move[1]

            if move[0] == 'L':
                for x in range(posX-1, posX-move[1], -1):
                    if self.a[posY][x] != '.':
                        self.a[posY][x] = 'X'
                        self.intersections.append([posY-oy,x-ox])
                    else:
                        self.a[posY][x] = '-'
                posX -= move[1]

            if move[0] == 'D':
                for y in range(posY-1, posY - move[1], -1):
                    if self.a[y][posX] != '.':
                        self.a[y][posX] = 'X'
                        self.intersections.append([y-oy,posX-ox])
                    else:
                        self.a[y][posX] = '|'
                posY -= move[1]

            self.a[posY][posX] = '+'



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

    def PrintMap(self):
        for row in reversed(self.a):
            print('.',' '.join([str(elem) for elem in row]), '.')
        print('. ' * (self.columns + 2))
        print(self.intersections)

    def PrintIntersections(self):
        print(self.intersections)

    def Manhattan(self, coord):
        return abs(coord[0]) + abs(coord[1])
        # return abs(int(coord[0]-int(self.columns/2))) + abs(int(coord[1])-int(self.rows/2))

    def FindClosest(self):
        distance = self.Manhattan(self.intersections[0])
        for c in self.intersections[1:]:
            if self.Manhattan(c) < distance:
                distance = self.Manhattan(c)
        return distance
