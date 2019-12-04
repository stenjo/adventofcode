# Advent of Code 2019: https://adventofcode.com/2019/day/5
# 
# 

from AoC05_classes import WireLine

infile = open('data/input_05.txt','r')
inputData1 = infile.readline().strip().split(',')
inputData2 = infile.readline().strip().split(',')

# Part 1
w = WireLine(20000,20000)
w.AddWireline(inputData1)
w.AddWireline(inputData2)
    
# act
# w.PrintIntersections()
result = w.FindClosest()
print("Part 1: ", result)
    
# Part 2

print("Part 2: ", w.FindFewerSteps())
    
