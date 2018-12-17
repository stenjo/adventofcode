# Advent of Code 2018: https://adventofcode.com/2018/day/17
#
# Tests

import unittest
from AoC17_classes import WaterFountain

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

    @unittest.skip('Not working')
    def test_move_unit(self):
        # arrange
        # bb = BeverageBandidts()
        goblin = Goblin(2,2)

        # act
        goblin.move(Direction(0,-1))    # up
        goblin.move(Direction(-1,0))    # left
        goblin.move(Direction(0,1))     # down
        goblin.move(Direction(1,0))    # right

        # assert
        self.assertEqual(goblin.position(), [2,2])

    # @unittest.skip('Not working')
    def test_findWalls(self):
        # arrange
        wf = WaterFountain()
        wf.load(test1)

        # act
        result = wf.findWalls(499,10)
        # assert
        self.assertEqual(result, [498,504])

    @unittest.skip('Not working')
    def test_directionTo(self):
        # arrange
        bb = BeverageBandidts()
        goblin = Goblin(2,2)
        elf00 = Elf(0,0)
        elf1010 = Elf(10,10)
        elf010 = Elf(0,10)
        elf100 = Elf(10,0)
        elf23 = Elf(2,3)

        result = []

        #act
        result.append(bb.directionTo(goblin, elf00).a())
        result.append(bb.directionTo(goblin, elf1010).a())
        result.append(bb.directionTo(goblin, elf010).a())
        result.append(bb.directionTo(goblin, elf100).a())
        result.append(bb.directionTo(goblin, elf23).a())

        # assert
        self.assertEqual(result, [[-1,-1],[1,1],[-1,1],[1,-1],[0,1]])

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

