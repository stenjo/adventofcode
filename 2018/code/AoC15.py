# Advent of Code 2018: https://adventofcode.com/2018/day/15
# 
# Main file

from AoC15_classes import BeverageBandidts

inputData = 409551


bb = BeverageBandidts()

scores = bb.getScores()

print('\nPart 1: The scores of the ten recipes immediately after', inputData, 'is', scores)

# print('\nPart 2: The location of the last cart is', cart.print())

