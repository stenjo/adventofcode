from Day02.matrix import max_min_difference, spreadsheet_checksum, evenly_divisible

def test_matrix():
    assert max_min_difference('5\t1\t9\t5') == 8
    assert max_min_difference('7\t5\t3') == 4
    assert max_min_difference('2\t4\t6\t8') == 6
    
    matrix = ['5\t1\t9\t5','7\t5\t3', '2\t4\t6\t8']
    
    assert spreadsheet_checksum(matrix) == 18
    
    inputData = open('../data/input2.txt','r')
    data = inputData.readlines()

    assert spreadsheet_checksum(data) == 46402

    matrix2 = ['5\t9\t2\t8','9\t4\t7\t3', '3\t8\t6\t5']
    
    assert evenly_divisible(matrix2) == 9
    
    assert evenly_divisible(data) == 265
