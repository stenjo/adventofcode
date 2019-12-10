# Advent of Code 2019: https://adventofcode.com/2019/day/10
# 
# 

from AoC10_classes import AsteroidMap

infile = open('data/input_10.txt','r')
inputData1 = infile.readlines()


# Part 1
w = AsteroidMap()
w.ReadMap(inputData1)
result = w.GetBestLOS()

print("Part 1: ", result)

# Part 2
result = w.RunAgain()
print("Part 2: ", result)
