#Test file for Advent of Code Day 3

import unittest
from AoC03_classes import WireLine

class WireCrossTest(unittest.TestCase):

    def setUp(self):
        return super().setUp()

    def test_print_map(self):
        # arrange
        testInput = ['R8','U5','L5','D3']
        testInput2 = ['U7','R6','D4','L4']
        w = WireLine(100,100)
        w.AddWireline(testInput)
        w.AddWireline(testInput2)

        # act
        # w.PrintMap()
        result = w.FindClosest()

        # assert
        self.assertEqual(result, 6)

    def test_distance_1(self):
        # arrange
        testInput1 = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
        testInput2 = ['U62','R66','U55','R34','D71','R55','D58','R83']
        w = WireLine(1000,1000)
        w.AddWireline(testInput1)
        w.AddWireline(testInput2)
            
        # act
        w.PrintIntersections()
        result = w.FindClosest()

        # assert
        self.assertEqual(result, 159)

    def test_distance_2(self):
        # arrange
        testInput1 = ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']
        testInput2 = ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']
        w = WireLine(1000,1000)
        w.AddWireline(testInput1)
        w.AddWireline(testInput2)
            
        # act
        w.PrintIntersections()
        result = w.FindClosest()

        # assert
        self.assertEqual(result, 135)

    def test_steps_1(self):
        # arrange
        testInput1 = ['R75','D30','R83','U83','L12','D49','R71','U7','L72']
        testInput2 = ['U62','R66','U55','R34','D71','R55','D58','R83']
        w = WireLine(1000,1000)
        w.AddWireline(testInput1)
        w.AddWireline(testInput2)
            
        # act
        # w.PrintIntersections()
        result = w.FindFewerSteps()

        # assert
        self.assertEqual(result, 610)

    def test_steps_2(self):
        # arrange
        testInput1 = ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51']
        testInput2 = ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']
        w = WireLine(1000,1000)
        w.AddWireline(testInput1)
        w.AddWireline(testInput2)
            
        # act
        # w.PrintIntersections()
        result = w.FindFewerSteps()

        # assert
        self.assertEqual(result, 410)

    
if __name__ == '__main__':
    unittest.main()
