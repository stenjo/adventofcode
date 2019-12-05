#Test file for Advent of Code Day 3

import unittest
from AoC05_classes import Compute

class RunComputeTest(unittest.TestCase):

    def setUp(self):
        return super().setUp()

    def test_compute_mode_1(self):
        # arrange
        testInput = [1002,4,3,4,33,99]
        w = Compute(testInput)

        # act
        result = w.RunCompute()

        # assert
        self.assertEqual(result[4], 99)
    
    def test_compute_mode_2(self):
        # arrange
        testInput = [1101,100,-1,4,0]
        w = Compute(testInput)

        # act
        result = w.RunCompute()

        # assert
        self.assertEqual(result[4], 99)

if __name__ == '__main__':
    unittest.main()
