# Advent of Code 2018: https://adventofcode.com/2018/day/16
#
# Tests

import unittest
from AoC16_classes import OpCodes

test1 = [
'Before: [3, 2, 1, 1]',
'9 2 1 2',
'After:  [3, 2, 2, 1]',
'',
'Before: [3, 3, 2, 1]',
'0 3 1 2',
'After:  [3, 3, 1, 1]',
'',
'Before: [3, 2, 2, 1]',
'5 3 2 1',
'After:  [3, 1, 2, 1]'
]

class OpCodeTest(unittest.TestCase):

    # @unittest.skip('Always true')
    def test_opcodes(self):
        # arrange
        # act
        # assert
        self.assertTrue(True)

    def test_load(self):
        # arrange
        oc = OpCodes()

        # act
        oc.load(test1)
        
        # assert
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()

