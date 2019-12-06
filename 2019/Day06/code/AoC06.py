# Advent of Code 2019: https://adventofcode.com/2019/day/6
# 
# 

from pprint import pprint
from AoC06_classes import Orbiter

infile = open('data/input_06.txt','r')
inputData1 = infile.readlines()

w = Orbiter(inputData1)

# Part 1
result = w.FindDistances()
print("Part 1: ", result)

# Part 2
result = w.FindSteps('YOU', 'SAN')
print("Part 2: ", result)
    
