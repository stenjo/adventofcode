# Advent of Code 2019: https://adventofcode.com/2019/day/12
# 
# 
import math, re


class Moon():

    pos = None
    vel = None
    name = None
    origin = None
    passedOrigin = False
    loopSteps = 0
    loopStepsXYZ = {'x':0, 'y':0, 'z':0}
    passedOriginXYZ  = {'x':False, 'y':False, 'z':False}

    def __init__(self, Name = None,  x=None, y=None, z=None, pos=None):
        super().__init__()
        self.pos = {'x':x, 'y':y, 'z':z}
        self.vel = {'x':0, 'y':0, 'z':0}
        self.origin = {'x':0, 'y':0, 'z':0}
        if pos != None:
            self.LoadMoon(pos)
        name = Name

    def LoadMoon(self, positionString):
        # '<x=2, y=-10, z=-7>'
        sc = set('<> ')
        pstrlist = ''.join([c for c in positionString if c not in sc]).split(',')
        for p in pstrlist:
            ps,val = p.split('=')
            self.pos[ps] = int(val)
            self.origin[ps] = int(val)
        self.loopSteps = 1
        self.loopStepsXYZ = {'x':0, 'y':0, 'z':0}
        self.passedOriginXYZ  = {'x':False, 'y':False, 'z':False}
        
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

    def TotalEnergy(self):
        return self.KineticEnergy() * self.PotentialEnergy()

    def IsAtOriginalPos(self):
        return self.pos == self.origin

    def Move(self):
        coords = 'xyz'
        for axis in coords:
            self.pos[axis] += self.vel[axis]
            if self.pos[axis] == self.origin[axis]: self.passedOriginXYZ[axis] = True 
            self.loopStepsXYZ[axis] += 1 if self.passedOriginXYZ[axis] == False else 0
        
        self.loopSteps += 1 if self.passedOrigin == False else 0

        if self.pos == self.origin: self.passedOrigin = True 

    def GetXYZFromString(self, pstring):
        sc = set('<> ')
        pstrlist = ''.join([c for c in pstring if c not in sc]).split(',')
        xyz = {}
        for p in pstrlist:
            ps,val = p.split('=')
            xyz[ps] = int(val)
        return xyz

    def GetXYZAsTuple(self, xyz):
        return (xyz['x'],xyz['y'],xyz['z'])
    
    def AsTuple(self):
        return (self.GetXYZAsTuple(self.pos),self.GetXYZAsTuple(self.vel))

    def GetXYZtuple(self, pstring):
        ps = self.GetXYZFromString(pstring)
        return self.GetXYZAsTuple(ps)
    
    def GetPosAndVelFromString(self, posvelstring):
        pos = re.search("pos=<(.*)>, ", posvelstring)
        pos = self.GetXYZtuple(pos.group(1))
        vel = re.search("vel=<(.*)>", posvelstring)
        vel = self.GetXYZtuple(vel.group(1))
        return (pos, vel)

class MoonMap():

    map = []

    def __init__(self, moonPositions = None):
        super().__init__()
        if moonPositions != None:
            self.LoadMoons(moonPositions)

    def LoadMoons(self, data):
        for d in data:
            m = Moon()
            m.LoadMoon(d)
            self.map.append(m)

    def CountMoons(self):
        return len(self.map)

    def TotalKinetic(self):
        total = 0
        for m in self.map:
            total += m.KineticEnergy()

        return total

    def TotalPotential(self):
        total = 0
        for m in self.map:
            total += m.PotentialEnergy()

        return total

    def TotalEnergy(self):
        total = 0
        for m in self.map:
            total += m.TotalEnergy()

        return total

    def Gravitate(self, a, b):
        coords = 'xyz'
        # print(a.AsTuple(),b.AsTuple())
        for axis in coords:
            if a.pos[axis] < b.pos[axis]:
                a.vel[axis] +=1
                b.vel[axis] -=1
            elif a.pos[axis] > b.pos[axis]:
                a.vel[axis] -=1
                b.vel[axis] +=1

    def OneStep(self):
        for i in range(len(self.map)):
            a = self.map[i]
            for n in range(i+1, len(self.map)):
                b = self.map[n]
                self.Gravitate(a,b)
        
        for a in self.map:
            a.Move()

    def AllAtOriginalPos(self):
        for a in self.map:
            if a.pos != a.origin:
                return False

        return True

    def AllWasAtOriginalPos(self):
        for a in self.map:
            if a.passedOrigin == False:
                return False

        return True
