#Test file for Advent of Code 2019: https://adventofcode.com/2019/day/6

import unittest
from AoC07_classes import Orbiter

class RunComputeTest(unittest.TestCase):

    def setUp(self):
        return super().setUp()

    def test_obritmap_1(self):
        # arrange
        testInput = ['COM)B','B)C','C)D','D)E','E)F','B)G','G)H','D)I','E)J','J)K','K)L']
        w = Orbiter(testInput)
        print(w.GetPlanet('L'))
        # act
        result = w.GetOrbits()
        result = w.FindDistances()
        # assert
        self.assertEqual(result, 42)
    
    def test_find_santa(self):
        # arrange
        testInput = ['COM)B','B)C','C)D','D)E','E)F','B)G','G)H','D)I','E)J','J)K','K)L','K)YOU','I)SAN']
        w = Orbiter(testInput)
        # print(w.GetPlanet('L'))
        # act
        result = w.GetOrbits()
        result = w.FindDistances()
        result = w.FindSteps('YOU', 'SAN')

        # assert
        self.assertEqual(result, 4)

if __name__ == '__main__':
    unittest.main()
