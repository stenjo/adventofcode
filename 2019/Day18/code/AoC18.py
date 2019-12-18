# Advent of Code 2019: https://adventofcode.com/2019/day/11
# 
# 

from AoC17_classes import Scaffoliding

infile = open('data/input_17.txt','r')
inputData1 = infile.readline().strip().split(',')

# Part 1
e = Scaffoliding(inputData1)
e.WriteScaff()
# e.PlotPanels()

# print("Part 1: ", e.NumberOfBlocks())

# Part 2
# result = w.RunAgain()
# print("Part 2: ", result)
