# Advent of Code 2023: https://adventofcode.com/2023/day/1
#
#
import re


def calibration(calibration_line):
    return int(get_first(calibration_line) + get_first(calibration_line[::-1]))


def get_first(str):
    m = re.search(r"\d", str)
    if m:
        return m[0]
    return "0"


def calibration_sum(strList):
    sum = 0
    for str in strList:
        sum += calibration(str)

    return sum


def spelled_out_calibration(calibration_line):
    spelled_out_line = spell_out(calibration_line)
    print(spelled_out_line, calibration(spelled_out_line))
    return calibration(spelled_out_line)


def spell_out(line):
    numbers = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in range(0, len(line)):
        for index, number in enumerate(numbers):
            if line[0 : i + 1].find(number) > -1:
                line = line.replace(number, str(index + 1))
    return line


def spelled_out_calibration_sum(str_list):
    sum = 0
    for str in str_list:
        sum += spelled_out_calibration(str)

    return sum
