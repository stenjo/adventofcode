# Advent of Code 2018: https://adventofcode.com/2018/day/13
# 
# Main file

from AoC13_classes import MineCart

inputData = open('../data/input13.txt','r')
liveData = inputData.readlines()
mc = MineCart()
mc.loadTracksAndCarts(liveData)
t = mc.track.validateAllTracks()
if t != None:
    print(t.print())
# mc.track.print()

crash = mc.findFirstCollision()

print('\nPart 1: The point of the first crash is', crash)

mc.loadTracksAndCarts(liveData)
cart = mc.findLastCart()

print('\nPart 2: The location of the last cart is', cart.print())

