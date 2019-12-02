# Advent of Code 2019: https://adventofcode.com/2019/day/2
# 
# 

from AoC02_classes import Compute

inputData = open('data/input_02.txt','r').readline().split(',')

# Part 1
sumOfFuel = 0
c = Compute(inputData)
result = c.Restore()
result = c.RunCompute()

print("Part 1: ", result[0])
    
# Part 2

print("Part 2: ", c.FindNounAndVerb(inputData))
    
