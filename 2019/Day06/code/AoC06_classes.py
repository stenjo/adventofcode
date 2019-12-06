# Advent of Code 2019: https://adventofcode.com/2019/day/6
# 
# 
import math

class Orbiter():

    orbitMap = []
    orbits = []
    planets = {}

    def __init__(self, data):
        self.LoadOrbits(data)
        self.ConvertOrbits()



    def LoadOrbits(self, data):
        self.orbitMap = list(map(str, data))

    def GetOrbits(self):
        return len(self.orbitMap)
        
    def ConvertOrbits(self):
        for o in self.orbitMap:
            center,satellite = o.strip().split(')')
            distance = 0
            self.orbits.append({'center':center, 'satellite':satellite, 'distance':distance})
        
        for p in self.orbits:
            planet = p['satellite']
            self.planets[p['satellite']] = p
        
        return
        
    def FindDistances(self):
        total = 0
        for p in self.orbits:
            total += self.Distance(p['satellite'])
        return total

    def Distance(self, planet):
        p = self.planets[planet]
        center = p['center']
        d = 1
        while "COM" not in center:
            c = self.planets[center]
            d += 1
            center = c['center']
        p['distance'] = d
        return d

    def FindSteps(self, you, santa):
        youTree = self.GetTree(you)
        santaTree = self.GetTree(santa)
        maxDistance = 0
        commomP = None
        # Find common
        for p in youTree:
            if p in santaTree:
                if maxDistance < self.planets[p]['distance']:
                    maxDistance = self.planets[p]['distance']
                    commomP = p
            
        return self.GetPlanet(you)['distance'] - maxDistance + self.GetPlanet(santa)['distance'] - maxDistance - 2


    def GetTree(self, planet):
        p = self.planets[planet]
        center = p['center']
        tree = []
        while "COM" not in center:
            tree.append(center)
            c = self.planets[center]
            center = c['center']
        return tree


    def GetPlanet(self, planet):
        return self.planets[planet]


