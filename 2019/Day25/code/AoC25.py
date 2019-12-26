# Advent of Code 2019: https://adventofcode.com/2019/day/11
# 
# 

from AoC25_classes import Droid


# Part 1
e = Droid()

code = input("instruction: ")
while True: #len(code) > 0:
    e.LoadAsciiProgram([code])
    result = e.RunProgram()
    print(result, end='')
    code = input(":> ")


print("Part 1: ", e.GetAffectedCells())

# Part 2
# result = w.RunAgain()
result = e.FindSquareDistance(100)
print("Part 2: ", result)
