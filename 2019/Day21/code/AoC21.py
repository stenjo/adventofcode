# Advent of Code 2019: https://adventofcode.com/2019/day/11
# 
# 

from AoC19_classes import SpaceMap

infile = open('data/input_19.txt','r')
inputData1 = infile.readline().strip().split(',')

# Part 1
e = SpaceMap(inputData1)
e.WriteTractorMap()

print("Part 1: ", e.GetAffectedCells())

# Part 2
# result = w.RunAgain()
result = e.FindSquareDistance(100)
print("Part 2: ", result)
