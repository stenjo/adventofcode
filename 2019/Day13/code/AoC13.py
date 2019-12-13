# Advent of Code 2019: https://adventofcode.com/2019/day/11
# 
# 

from AoC13_classes import ArcadeCabinet

infile = open('data/input_13.txt','r')
inputData1 = infile.readline().strip().split(',')

# Part 1
e = ArcadeCabinet(inputData1)
e.RunGame()
# e.PlotPanels()

print("Part 1: ", e.NumberOfBlocks())

# Part 2
# result = w.RunAgain()
# print("Part 2: ", result)
