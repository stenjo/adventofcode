import pytest

from Day01.captcha import sum_of_all_matching_next, sum_halfway_around

inputData = open('../data/input1.txt','r')
def test_captcha():
    assert sum_of_all_matching_next('1122') == 3
    assert sum_of_all_matching_next('1111') == 4
    assert sum_of_all_matching_next('1234') == 0
    assert sum_of_all_matching_next('91212129') == 9
    
    data = inputData.readlines()[0].strip()
    assert sum_of_all_matching_next(data) == 1031

    assert sum_halfway_around('1212') == 6
    assert sum_halfway_around('1221') == 0
    assert sum_halfway_around('123425') == 4
    assert sum_halfway_around('123123') == 12
    assert sum_halfway_around('12131415') == 4
    
    assert sum_halfway_around(data) == 1080
