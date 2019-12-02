#Test file for Advent of Code Day 2

import unittest
from AoC02_classes import Compute

class ComputeTest(unittest.TestCase):

    def setUp(self):
        return super().setUp()

    def test_compute_program_0(self):
        # arrange
        testInput = [1,9,10,3,2,3,11,0,99,30,40,50]
        testResult = [3500,9,10,70,2,3,11,0,99,30,40,50]
        c = Compute(testInput)
            
        # act
        result = c.RunCompute()

        # assert
        self.assertEqual(result, testResult)

    def test_compute_program_1(self):
        # arrange
        testInput = [1,0,0,0,99]
        testResult = [2,0,0,0,99]
        c = Compute(testInput)
            
        # act
        result = c.RunCompute()

        # assert
        self.assertEqual(result, testResult)

    def test_compute_program_2(self):
        # arrange
        testInput = [2,3,0,3,99]
        testResult = [2,3,0,6,99]
        c = Compute(testInput)
            
        # act
        result = c.RunCompute()

        # assert
        self.assertEqual(result, testResult)

    def test_compute_program_3(self):
        # arrange
        testInput = [2,4,4,5,99,0]
        testResult = [2,4,4,5,99,9801]
        c = Compute(testInput)
            
        # act
        result = c.RunCompute()

        # assert
        self.assertEqual(result, testResult)

    def test_compute_program_4(self):
        # arrange
        testInput = [1,1,1,4,99,5,6,0,99]
        testResult = [30,1,1,4,2,5,6,0,99]
        c = Compute(testInput)
            
        # act
        result = c.RunCompute()

        # assert
        self.assertEqual(result, testResult)

    # def test_calculate_fuel_with_fuel(self):
    #     # arrange
    #     testData = {12:2, 14:2, 1969:966, 100756:50346}

    #     for testMass in testData:
                
    #         # act
    #         result = self.fuel.CalculateFuelWithFuel(testMass)

    #         # assert
    #         self.assertEqual(result, testData[testMass])
    
if __name__ == '__main__':
    unittest.main()
