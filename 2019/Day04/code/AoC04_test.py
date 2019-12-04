#Test file for Advent of Code Day 4

import unittest
from AoC04_classes import FindPassword

class PasswordTest(unittest.TestCase):

    def setUp(self):
        return super().setUp()

    def test_six_digit(self):
        # arrange
        testInputLow = 23588
        testInputHigh = 2346677
        testInputCorrect = 122334

        f = FindPassword()

        # act
        low = f.Length(testInputLow)
        high = f.Length(testInputHigh)
        correct = f.Length(testInputCorrect)

        # assert
        self.assertFalse(low)
        self.assertFalse(high)
        self.assertTrue(correct)

    def test_below_range(self):
        # arrange
        testRange = '111111-223450'
        testInput1 = 111110
        f = FindPassword(testRange)
           
        # act
        result = f.IsWithinRange(testInput1)

        # assert
        self.assertFalse(result)

    def test_above_range(self):
        # arrange
        testRange = '111111-223450'
        testInput2 = 223456
        f = FindPassword(testRange)
           
        # act
        result = f.IsWithinRange(testInput2)

        # assert
        self.assertFalse(result)

    def test_within_range(self):
        # arrange
        testRange = '111111-223450'
        testInput1 = 111111
        testInput2 = 223459
        testInput3 = 123456
        f = FindPassword(testRange)
           
        # act
        result = f.IsWithinRange(testInput3)

        # assert
        self.assertTrue(result)

    def test_adjacent_true_1(self):
        # arrange
        testInput1 = 111111
        f = FindPassword()
           
        # act
        result = f.HasAdjacent(testInput1)

        # assert
        self.assertTrue(result)

    def test_adjacent_true_2(self):
        # arrange
        testInput2 = 223459
        f = FindPassword()
           
        # act
        result = f.HasAdjacent(testInput2)

        # assert
        self.assertTrue(result)

    def test_adjacent_false(self):
        # arrange
        testInput3 = 123456
        f = FindPassword()
           
        # act
        result = f.HasAdjacent(testInput3)

        # assert
        self.assertFalse(result)

    def test_decreasing_number_no(self):
        # arrange
        testInput2 = 223454
        f = FindPassword()
           
        # act
        result = f.Increasing(testInput2)

        # assert
        self.assertFalse(result)

    def test_decreasing_number_low(self):
        # arrange
        testInput1 = 111111
        f = FindPassword()
           
        # act
        result = f.Increasing(testInput1)

        # assert
        self.assertTrue(result)

    def test_decreasing_number_high(self):
        # arrange
        testInput3 = 123459
        f = FindPassword()
           
        # act
        result = f.Increasing(testInput3)

        # assert
        self.assertTrue(result)

    def test_is_valid_1(self):
        # arrange
        testInput = 111111
        f = FindPassword()
           
        # act
        result = f.Increasing(testInput)

        # assert
        self.assertTrue(result)

    def test_is_valid_2(self):
        # arrange
        testInput = 223450
        f = FindPassword()
           
        # act
        result = f.IsValid(testInput)

        # assert
        self.assertFalse(result)

    def test_is_valid_3(self):
        # arrange
        testInput = 123789
        f = FindPassword()
           
        # act
        result = f.IsValid(testInput)

        # assert
        self.assertFalse(result)

    def test_int_to_array_convert(self):
        # arrange
        testInput = 123089
        f = FindPassword()
           
        # act
        result = f.ArrayToInt(f.IntToArray(testInput))

        # assert
        self.assertEqual(result, testInput)

    def test_adjacent_nl_true_1(self):
        # arrange
        testInput1 = 112233
        f = FindPassword()
           
        # act
        result = f.HasAdjacentNL(testInput1)

        # assert
        self.assertTrue(result)

    def test_adjacent_nl_true_2(self):
        # arrange
        testInput1 = 123444
        f = FindPassword()
           
        # act
        result = f.HasAdjacentNL(testInput1)

        # assert
        self.assertFalse(result)

    def test_adjacent_nl_true_3(self):
        # arrange
        testInput1 = 111122
        f = FindPassword()
           
        # act
        result = f.HasAdjacentNL(testInput1)

        # assert
        self.assertTrue(result)

    
if __name__ == '__main__':
    unittest.main()
