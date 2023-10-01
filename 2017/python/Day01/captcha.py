# Advent of Code 2017: https://adventofcode.com/2017/day/1
# 
# 

def sum_of_all_matching_next(numbers):
    checksum = 0
    for i in range(len(numbers)):
        if numbers[i] == numbers[(i+1) % len(numbers)]:
            checksum += int(numbers[i])

    return checksum

def sum_halfway_around(numbers):
    checksum = 0
    offset = int(len(numbers)/2)
    for i in range(len(numbers)):
        if numbers[i] == numbers[(i+offset) % len(numbers)]:
            checksum += int(numbers[i])

    return checksum