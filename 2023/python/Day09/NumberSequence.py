# Advent of Code 2023: https://adventofcode.com/2023/day/9
#
#
from functools import reduce


class NumberSequence:
    def __init__(self, input=[]):
        self.sequences = []
        if len(input) > 0:
            self.sequences = [
                [int(n) for n in nList]
                for nList in [seqStr.split() for seqStr in input]
            ]

    def newSequence(self, nums):
        return [nums[i + 1] - a for i, a in enumerate(nums) if i < len(nums) - 1]

    def allZeros(self, sequence):
        return all(v == 0 for v in sequence)

    def nextNumber(self, nums):
        if self.allZeros(self.newSequence(nums)) == False:
            return nums[-1] + self.nextNumber(self.newSequence(nums))

        return nums[-1]

    def previousNumber(self, nums):
        if self.allZeros(self.newSequence(nums)) == False:
            return nums[0] - self.previousNumber(self.newSequence(nums))

        return nums[0]

    def sumOfNextNumbers(self):
        return sum([self.nextNumber(numbers) for numbers in self.sequences])

    def sumOfPreviousNumbers(self):
        return sum([self.previousNumber(numbers) for numbers in self.sequences])
