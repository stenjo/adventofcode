# Advent of Code 2019: https://adventofcode.com/2019/day/9
# 
# 

from pprint import pprint
from AoC09_classes import Compute

infile = open('data/input_09.txt','r')
inputData1 = infile.readline().strip().split(',')


# Part 1
w = Compute(inputData1)
w.LoadInput([1])
w.LoadProgram(inputData1)
result = w.RunCompute()

print("Part 1: ", result)

# Part 2
w.LoadInput([2,result])
w.LoadProgram(inputData1)
result = w.RunCompute()
print("Part 2: ", result)
