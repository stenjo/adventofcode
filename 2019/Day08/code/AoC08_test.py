#Test file for Advent of Code 2019: https://adventofcode.com/2019/day/6

import unittest
from AoC08_classes import Mapper

class RunMapTest(unittest.TestCase):

    def setUp(self):
        return super().setUp()

    def test_lowest_zeros_1(self):
        # arrange
        testInput = '123456789012'
        w = Mapper(testInput, '3x2')

        # act
        result = w.LowestZeros()

        # assert
        self.assertEqual(result['layer']+1, 1)
    
    def test_lowest_zeros_2(self):
        # arrange
        testInput = '121112002012'
        w = Mapper(testInput, '3x2')

        # act
        result = w.LowestZeros()

        # assert
        self.assertEqual(result['layer']+1, 1)
    
    def test_one_by_twos(self):
        # arrange
        testInput = '121112002012'
        w = Mapper(testInput, '3x2')
        result = []

        # act
        result.append(w.GetOneByTwos(1))
        result.append(w.GetOneByTwos(2))

        # assert
        self.assertEqual(result, [8, 2])
    
    def test_find_onebytwos_on_lowest_zero_layer(self):
        # arrange
        testInput = '121112002012'
        w = Mapper(testInput, '3x2')

        # act
        result = w.Find1x2OnLowest0()

        # assert
        self.assertEqual(result, 8)

    def test_find_onebytwos_on_lowest_zero_layer_live(self):
        # arrange
        infile = open('data/input_08.txt','r')
        testInput = infile.readline()
        w = Mapper(testInput, '25x6')

        # act
        result = w.Find1x2OnLowest0()

        # assert
        self.assertEqual(result, 2210)


    def test_layer_pixels(self):
        # arrange
        testInput = '0222112222120000'
        w = Mapper(testInput, '2x2')
        result = []

        # act
        for p in range(4):
            result.append(w.GetPixelAt(p))

        # assert
        self.assertEqual(result, [' ', '*', '*', ' '])


if __name__ == '__main__':
    unittest.main()
