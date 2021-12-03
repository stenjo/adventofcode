# Advent of Code 2018: https://adventofcode.com/2018/day/14
# 
# Main file

from AoC14_classes import ChocoChart

inputData = 409551


cc = ChocoChart()

scores = cc.getScores()

print('\nPart 1: The scores of the ten recipes immediately after', inputData, 'is', scores)

# print('\nPart 2: The location of the last cart is', cart.print())

