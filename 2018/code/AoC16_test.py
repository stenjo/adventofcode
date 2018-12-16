# Advent of Code 2018: https://adventofcode.com/2018/day/15
#
# Tests

import unittest
from AoC16_classes import OpCodes

test1 = [
'Before: [3, 2, 1, 1]',
'9 2 1 2',
'After:  [3, 2, 2, 1]',
]

class OpCodeTest(unittest.TestCase):

    # @unittest.skip('Always true')
    def test_opcodes(self):
        # arrange
        # act
        # assert
        self.assertTrue(True)


if __name__ == '__main__':
    unittest.main()

