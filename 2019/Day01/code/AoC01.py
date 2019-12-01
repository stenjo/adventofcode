# Advent of Code 2019: https://adventofcode.com/2019/day/1
# 
# 

from AoC01_classes import Fuel

inputData = open('data/input_01.txt','r').readlines()

# Part 1
sumOfFuel = 0
f = Fuel()
for moduleMass in inputData:
    m = int(moduleMass.strip())
    fuel =  f.CalculateFuel(m)
    sumOfFuel += fuel

print("Part 1: ", sumOfFuel)
    
# Part 2
sumOfFuel = 0
f = Fuel()
for moduleMass in inputData:
    m = int(moduleMass.strip())
    fuel =  f.CalculateFuelWithFuel(m)
    sumOfFuel += fuel

print("Part 2: ", sumOfFuel)
    
