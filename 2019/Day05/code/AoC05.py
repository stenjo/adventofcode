# Advent of Code 2019: https://adventofcode.com/2019/day/5
# 
# 

from AoC05_classes import WireLine

infile = open('data/input_05.txt','r')
inputData1 = infile.readline().strip().split(',')
inputData2 = infile.readline().strip().split(',')

# Part 1
w = WireLine()
w.AddWireline(inputData1)
w.AddWireline(inputData2)
    
# act
print("Part 1: ", w.FindClosest())
    
# Part 2
print("Part 2: ", w.FindFewerSteps())
    
