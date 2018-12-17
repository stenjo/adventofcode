#Test file for Advent of Code Day 10
import unittest
from AoC10_classes import Point,SkyMap

class MessageTest(unittest.TestCase):

    def setUp(self):
        self.skyMap = SkyMap()
        self.pArra  = [ [[ 0, 0],[-1, 1]], 
                        [[-1,-1],[-2,-2]] , 
                        [[10,-2],[10, 2]] , 
                        [[-0,20],[-2,-2]] , 
                        [[ 2, 0],[20,20]]   ]
        self.points = [Point(p) for p in self.pArra]

        ref     = [ [[-1, 1],[-1, 1]], 
                    [[-3,-3],[-2,-2]] , 
                    [[20, 0],[10, 2]] , 
                    [[-2,18],[-2,-2]] , 
                    [[22,20],[20,20]]  ]
        self.reference = [Point(r) for r in ref]

        self.skyMap.load(self.pArra)

    def test_manhattan(self):
        # arrange
        result = []

        # act
        for i in range(len(self.points)):
            result.append( self.points[i].manhattan( self.points[ (i+1) % len(self.points) ] )) 

        # assert
        self.assertEqual(result, [ 2, 12, 32, 22, 2])

    def test_move_point_one_second(self):
        # arrange
        self.skyMap.dispose()
        self.skyMap.load(self.pArra)
        # act
        #assert
        for i in range(len(self.points)):
            p = self.points[i]
            p.moveOneSecond()
            self.assertTrue(p.equals(self.reference[i]))

    # @unittest.skip("not working")
    def test_manhattan_of_list(self):
        # arrange
        self.skyMap.dispose()
        self.skyMap.load(self.pArra)

        # act
        result = self.skyMap.getManhattanOfList()

        #assert
        self.assertEqual(result, 36+40+66+96+38)

    def test_move_one_second(self):
        # arrange
        # act
        self.skyMap.moveOneSecond()
        
        # assert
        for i in range(len(self.points)):
            r = self.reference[i]
            p = self.skyMap.Map[i]
            self.assertTrue(p.equals(r))


if __name__ == '__main__':
    unittest.main()
