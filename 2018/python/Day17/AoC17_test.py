# Advent of Code 2018: https://adventofcode.com/2018/day/17
#
# Tests

import unittest
from AoC17_classes import WaterFountain, Width

test1 = [
'x=495, y=2..7',
'y=7, x=495..501',
'x=501, y=3..7',
'x=498, y=2..4',
'x=506, y=1..2',
'x=498, y=10..13',
'x=504, y=10..13',
'y=13, x=498..504'
]

#    4444445555555
#    9999990000000
#    4567890123456
#  0       +       
#  1       |     # 
#  2  #  # |     # 
#  3  #  #~~#      
#  4  #  #~~#      
#  5  #~~~~~#      
#  6  #~~~~~#      
#  7  #######      
#  8               
#  9               
# 10     #     #   
# 11     #     #   
# 12     #     #   
# 13     #######   
# 14               

class WaterFountainTest(unittest.TestCase):

    def test_waterfountain(self):
        # arrange
        # act
        # assert
        self.assertTrue(True)

    # @unittest.skip('Not working')
    def test_load_data_wf(self):
        # arrange
        wf = WaterFountain()

        # act
        wf.load(test1)
        result = wf.getGridItem(495,7)

        # assert
        self.assertEqual(result, '#')

    # @unittest.skip('Not working')
    def test_putGridItem(self):
        # arrange
        wf = WaterFountain()
        
        # act
        wf.putGridItem('t', 2, 2)

        # assert
        self.assertEqual(wf.getGridItem(2,2), 't')

    # @unittest.skip('Not working')
    def test_tryDown(self):
        # arrange
        wf = WaterFountain()

        # act
        wf.load(test1)
        wf.tryDown(500,0)

        # assert
        wf.printGrid()

        self.assertTrue(True)

    # @unittest.skip('Not working')
    def test_findWalls(self):
        # arrange
        wf = WaterFountain()
        wf.load(test1)

        # act
        result = wf.findWalls(499,10)
        # assert
        self.assertEqual(result.a, [498,504])

    # @unittest.skip('Not working')
    def test_findEdge(self):
        # arrange
        wf = WaterFountain()
        wf.load(test1)

        # act
        result = wf.findEdge(500,2)
        # assert
        self.assertEqual(result.a, [499,502])

    # @unittest.skip('Not working')
    def test_do_fill_with_water(self):
        # arrange
        wf = WaterFountain()

        # act
        wf.load(test1)
        wf.doFillWithWater()

        # assert
        wf.printGrid()

        self.assertTrue(True)


    # @unittest.skip('Not needed')
    def test_grid_print(self):
        # arrange
        wf = WaterFountain()

        # act
        wf.load(test1)

        # assert
        wf.printGrid()

        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()

