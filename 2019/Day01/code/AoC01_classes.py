# Advent of Code 2019: https://adventofcode.com/2019/day/1
# 
# 
import math

class Fuel():
    
    def CalculateFuel(self, mass):
        return math.floor(mass/3) - 2

    def CalculateFuelWithFuel(self, mass):
        sumOfFuel = 0
        fuel = mass
        while fuel >= 0:
            fuel = self.CalculateFuel(fuel)
            if fuel > 0:
                sumOfFuel += fuel

        return sumOfFuel



