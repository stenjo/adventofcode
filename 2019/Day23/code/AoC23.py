# Advent of Code 2019: https://adventofcode.com/2019/day/11
# 
# 

from AoC23_classes import NetworkInterfaceController

infile = open('data/input_23.txt','r')
program = infile.readline().strip().split(',')

# Part 1
e = NetworkInterfaceController(program)        
print("Part 1: ", e.RunComputers())

# Part 2
infile = open('data/input_23.txt','r')
program = infile.readline().strip().split(',')
f = NetworkInterfaceController(program)
result = f.RunForNAT()
print("Part 2: ", result)
