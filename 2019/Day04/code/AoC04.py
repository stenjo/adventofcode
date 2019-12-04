# Advent of Code 2019: https://adventofcode.com/2019/day/4
# 
# 

from AoC04_classes import FindPassword

inputData1 = '138241-674034'

# Part 1
f = FindPassword(inputData1)
    
# act
result = f.Passwords()
print("Part 1: ", result)
    
# Part 2
result = f.PasswordsNL()
print("Part 2: ", result)
    
