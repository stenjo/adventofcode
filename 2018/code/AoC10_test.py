#Test file for Advent of Code Day 10
import unittest
from AoC10 import Point,SkyMap

class MessageTest(unittest.TestCase):
    def test_manhattan(self):
        # arrange
        points = [Point([0,0],[1,1]), Point([0,2],[2,2])]

        # act
        result = points[0].manhattan(points[1])

        # assert
        self.assertEqual(result, 3)
        # self.assertEqual(result, [ 4, 2, 37 ])

    def test_move_one_second(self):
        # arrange
        points = [Point([0,0],[-1,1]), Point([0,2],[2,2])]
        m = SkyMap(points)

        # act
        result = m.moveOneSecond()
        
        # assert
        self.assertEqual(result, 3)


if __name__ == '__main__':
    unittest.main()
