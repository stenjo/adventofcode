# Advent of Code 2019: https://adventofcode.com/2019/day/11
# 
# 

from AoC11_classes import EmHullPaRob

infile = open('data/input_11.txt','r')
inputData1 = infile.readline().strip().split(',')

# Part 1
e = EmHullPaRob(inputData1)
e.PlotPanels()

print("Part 1: ", e.NumberOfPanelsPainted())

# Part 2
# result = w.RunAgain()
# print("Part 2: ", result)
