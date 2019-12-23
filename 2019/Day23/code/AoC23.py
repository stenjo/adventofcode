# Advent of Code 2019: https://adventofcode.com/2019/day/11
# 
# 

from AoC23_classes import NetworkInterfaceController

infile = open('data/input_23.txt','r')
program = infile.readline().strip().split(',')

# Part 1
e = NetworkInterfaceController(program)

print("Part 1: ", len(e.computers))

# Part 2
# result = w.RunAgain()
# result = e.FindSquareDistance(100)
print("Part 2: ", len(e.computers))
