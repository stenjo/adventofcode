# Advent of Code 2019: https://adventofcode.com/2019/day/12
# 
# 

from pprint import pprint
from AoC12_classes import Moon, MoonMap

infile = open('data/input_12.txt','r')
inputData1 = infile.readlines()

w = MoonMap(inputData1)

for i in range(1000):
    w.OneStep()

t = w.TotalEnergy()

# Part 1
print("Part 1: ", t)

# Part 2
print("Part 2: ")
# w.PrintImage()
