# Advent of Code 2019: https://adventofcode.com/2019/day/5
# 
# 

from pprint import pprint
from AoC05_classes import Compute

infile = open('data/input_05.txt','r')
inputData1 = infile.readline().strip().split(',')

# Part 1
w = Compute(inputData1)

w.LoadInput([1])
result = w.RunCompute()
pprint(w.GetOutputs())    
# act
print("Part 1: ", result[len(result)-1])
    
# Part 2
# print("Part 2: ", w.FindFewerSteps())
    
