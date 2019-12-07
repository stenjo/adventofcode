# Advent of Code 2019: https://adventofcode.com/2019/day/7
# 
# 

from pprint import pprint
from AoC07_classes import AmplificationCircuit

infile = open('data/input_07.txt','r')
inputData1 = infile.readline().split(',')

w = AmplificationCircuit(0,inputData1)

# Part 1
result = w.GetMaxAmplification()
print("Part 1: ", result)

# Part 2
result = w.GetMaxLoopbackAmp()
print("Part 2: ", result)
    
