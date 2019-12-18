# Advent of Code 2019: https://adventofcode.com/2019/day/18
# 
# 

import inspect

class Labyrinth():

    map = {}
    mKeys = {}
    mDoors = {}
    pos = None

    def __init__(self, map):
        super().__init__()

        self.LoadMap(map)

    def LoadMap(self, map):
        y = 0
        for l in map:
            x = 0
            for p in l.strip():
                self.map[(x,y)] = p
                if p.isalpha():
                    if p.isupper():
                        self.mDoors[p] = {'pos':(x,y)}
                    else:
                        self.mKeys[p] = {'pos':(x,y)}
                if p == '@':
                    self.pos = (x,y)
                x += 1
            y += 1

    def PrintMap(self, current):
        w,h = max(self.map)
        for y in range(h+1):
            line = []
            for x in range(w+1):
                if (x,y) == self.pos:
                    line.append('@')
                elif (x,y) == current:
                    line.append('X')
                else:
                    line.append(self.map[(x,y)])

            print(''.join([n for n in line]))

    def GetDoors(self):
        return self.mDoors.keys()

    def GetKeys(self):
        return self.mKeys.keys()

    def GetSteps(self, item):
        found = False
        pos = self.pos
        steps = 0
        direction = (1,0)
        x,y = pos
        track = []
        while found == False:
            if (x,y) in track:
                dx,dy = direction
                x = x-dx
                y = y-dy
                steps -= 1
            else:
                p = self.map[(x,y)] 
                if p == item:
                    found = True
                elif p == '.':
                    steps += 1
                elif p == '#':  # Change direction
                    dx,dy = direction
                    x = x-dx
                    y = y-dy
                    if direction == (1,0):
                        direction = (0,1)
                    elif direction == (0,1):
                        direction = (-1,0)
                    elif direction == (-1,0):
                        direction = (0,-1)
                    else:
                        direction = (1,0)
                track.append((x,y))
                # next step
                dx,dy = direction
                x = x + dx
                y = y + dy
            
            self.PrintMap((x,y))
            print(steps)

        return steps

    def GetStepsToSpace(self, coord):
        return

