# Advent of Code 2018: https://adventofcode.com/2018/day/17
#
# Tests

import unittest
from AoC17_classes import BeverageBandidts, Goblin, Elf, Direction

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

    def test_beveragebandidts(self):
        # arrange
        # act
        # assert
        self.assertTrue(True)

    # @unittest.skip('Not working')
    def test_load_data(self):
        # arrange
        bb = BeverageBandidts()

        # act
        bb.load(test1)

        # assert
        self.assertEqual(bb.numGoblins(), 8)
        self.assertEqual(bb.numElfs(), 2)
        self.assertEqual(bb.numGoblins(), 8)

    def test_putGridItem(self):
        # arrange
        bb = BeverageBandidts()
        
        # act
        bb.putGridItem('t', 2, 2)

        # assert
        self.assertEqual(bb.getGridItem(2,2), 't')

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

    def test_distanceTo(self):
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
        result.append(bb.distanceTo(goblin, elf00))
        result.append(bb.distanceTo(goblin, elf1010))
        result.append(bb.distanceTo(goblin, elf010))
        result.append(bb.distanceTo(goblin, elf100))
        result.append(bb.distanceTo(goblin, elf23))

        # assert
        self.assertEqual(result, [4,16,10,10,1])

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

    def test_get_nearest(self):
        # arrange
        bb=BeverageBandidts()
        bb.load(test1)
        result = []
        # act
        goblin11 = bb.getUnitAt(1,1)
        result.append(bb.getNearestTo(goblin11))
        goblin77 = bb.getUnitAt(7,7)
        result.append(bb.getNearestTo(goblin77))

        # assert
        self.assertEqual(result, [bb.getUnitAt(4,4), bb.getUnitAt(4,5)])


    # @unittest.skip('Not needed')
    def test_grid_print(self):
        # arrange
        bb = BeverageBandidts()

        # act
        bb.load(test1)

        # assert
        bb.printGrid()
        bb.doRound()
        bb.printGrid()

        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()

