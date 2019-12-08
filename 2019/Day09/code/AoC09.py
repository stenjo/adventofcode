# Advent of Code 2019: https://adventofcode.com/2019/day/9
# 
# 

from pprint import pprint
from AoC09_classes import Mapper

infile = open('data/input_09.txt','r')
inputData1 = infile.readline()

w = Mapper(inputData1, '25x6')

# Part 1
print("Part 1: ", w.Find1x2OnLowest0())

# Part 2
print("Part 2: ")
w.PrintImage()
