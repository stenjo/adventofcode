import pytest

from Day01.calibration import (
    calibration,
    calibration_sum,
    spell_out,
    spelled_out_calibration,
    spelled_out_calibration_sum,
)

inputData = open("../data/input01.txt", "r")
inputData2 = open("../data/input01.txt", "r")
testInputData = open("../data/test_input01.txt", "r")
test2InputData = open("../data/test2_input01.txt", "r")


def test_calibration():
    assert calibration("1abc2") == 12
    assert calibration("pqr3stu8vwx") == 38
    assert calibration("a1b2c3d4e5f") == 15
    assert calibration("treb7uchet") == 77
    assert calibration("7") == 77
    assert calibration("77") == 77
    assert calibration("") == 0
    assert calibration("abcdefgh") == 0

    assert calibration_sum(testInputData) == 142
    assert calibration_sum(inputData) == 55123


def test_spell_out():
    assert spell_out("two1nine") == "219"
    assert spell_out("eightwothree") == "823"
    assert spell_out("abcone2threexyz") == "123"
    assert spell_out("sevenine") == "79"
    assert spell_out("eighthree") == "83"


def test_spelled_out_calibration():
    assert spelled_out_calibration("two1nine") == 29
    assert spelled_out_calibration("eightwothree") == 83
    assert spelled_out_calibration("abcone2threexyz") == 13
    assert spelled_out_calibration("xtwone3four") == 24
    assert spelled_out_calibration("4nineeightseven2") == 42
    assert spelled_out_calibration("zoneight234") == 14
    assert spelled_out_calibration("7pqrstsixteen") == 76


def test_spelled_out_calibration_sum():
    assert spelled_out_calibration_sum(test2InputData) == 281
    assert spelled_out_calibration_sum(inputData2) == 55260
