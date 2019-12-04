#Test file for Advent of Code Day 3

import unittest
from AoC05_classes import WireLine

class WireCrossTest(unittest.TestCase):

    def setUp(self):
        return super().setUp()

    def test_print_map(self):
        # arrange
        testInput = ['R8','U5','L5','D3']
        w = WireLine(100,100)
        w.AddWireline(testInput)

        # act
        result = w.FindClosest()

        # assert
        self.assertEqual(result, 6)
    
if __name__ == '__main__':
    unittest.main()
