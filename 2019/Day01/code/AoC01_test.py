#Test file for Advent of Code Day 1

import unittest
from AoC01_classes import Fuel

class FuelTest(unittest.TestCase):

    def setUp(self):
        self.fuel = Fuel()

    def test_calculate_fuel(self):
        # arrange
        testdata = {12:2, 14:2, 1969:654, 100756:33583}

        for testMass in testdata:
                
            # act
            result = self.fuel.CalculateFuel(testMass)

            # assert
            self.assertEqual(result, testdata[testMass])

    def test_calculate_fuel_with_fuel(self):
        # arrange
        testData = {12:2, 14:2, 1969:966, 100756:50346}

        for testMass in testData:
                
            # act
            result = self.fuel.CalculateFuelWithFuel(testMass)

            # assert
            self.assertEqual(result, testData[testMass])




    
if __name__ == '__main__':
    unittest.main()
