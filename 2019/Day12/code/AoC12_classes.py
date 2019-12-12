# Advent of Code 2019: https://adventofcode.com/2019/day/12
# 
# 
import math


class Moon():

    pos = None
    vel = None
    name = None

    def __init__(self, Name = None,  x=None, y=None, z=None):
        super().__init__()
        self.pos = {'x':x, 'y':y, 'z':z}
        self.vel = {'x':0, 'y':0, 'z':0}
        name = Name

    def LoadMoon(self, positionString):
        # '<x=2, y=-10, z=-7>'
        sc = set('<> ')
        pstrlist = ''.join([c for c in positionString if c not in sc]).split(',')
        for p in pstrlist:
            ps,val = p.split('=')
            self.pos[ps] = int(val)
        
    def SetVelocity(self, vel):
        sc = set('<> ')
        pstrlist = ''.join([c for c in vel if c not in sc]).split(',')
        for p in pstrlist:
            ps,val = p.split('=')
            self.vel[ps] = int(val)

    def PotentialEnergy(self):
        return abs(self.pos['x'])+abs(self.pos['y'])+abs(self.pos['z'])

    def KineticEnergy(self):
        return abs(self.vel['x'])+abs(self.vel['y'])+abs(self.vel['z'])

    def Move(self):
        coords = 'xyz'
        for axis in coords:
         self.pos[axis] += self.vel[axis]


    def GetXYZFromString(self, pstring):
        sc = set('<> ')
        pstrlist = ''.join([c for c in pstring if c not in sc]).split(',')
        xyz = {}
        for p in pstrlist:
            ps,val = p.split('=')
            xyz[ps] = int(val)
        return xyz

    def GetXYSAsTuple(self, xyz):
        return (xyz['x'],xyz['y'],xyz['z'])

class MoonMap():

    map = []

    def __init__(self, moonPositions):
        super().__init__()
        self.LoadMoons(moonPositions)

    def LoadMoons(self, data):
        for d in data:
            m = Moon()
            m.LoadMoon(d)
            self.map.append(m)

    def CountMoons(self):
        return len(self.map)

    def Gravitate(self, a, b):
        coords = 'xyz'
        for axis in coords:
            if a.pos[axis] < b.pos[axis]:
                a.vel[axis] +=1
                b.vel[axis] -=1
            elif a.pos[axis] > b.pos[axis]:
                a.vel[axis] +=1
                b.vel[axis] -=1

    def OneStep(self):
        for a in self.map:
            for b in self.map:
                self.Gravitate(a,b)
        
        for a in self.map:
            a.Move()