# Advent of Code 2018: https://adventofcode.com/2018/day/15
#
# Tests

import unittest
from AoC15_classes import BeverageBandidts, Goblin, Elf

test1 = [
'#########',
'#G..G..G#',
'#.......#',
'#.......#',
'#G..E..G#',
'#.......#',
'#.......#',
'#G..G..G#',
'#########'
]

class BeverageBandidtsTest(unittest.TestCase):

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
        self.assertEqual(bb.numElfs(), 1)
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
        goblin.move('up')
        goblin.move('left')
        goblin.move('down')
        goblin.move('right')

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
        result.append(bb.directionTo(goblin, elf00))
        result.append(bb.directionTo(goblin, elf1010))
        result.append(bb.directionTo(goblin, elf010))
        result.append(bb.directionTo(goblin, elf100))
        result.append(bb.directionTo(goblin, elf23))

        # assert
        self.assertEqual(result, [[-1,-1],[1,1],[-1,1],[1,-1],[0,1]])

    def test_get_nearest(self):
        # arrange
        bb=BeverageBandidts()
        bb.load(test1)
        result = None
        # act
        goblin = bb.getUnitAt(2,2)
        result = bb.getNearest(goblin)

        # assert
        self.assertEqual(result, bb.getUnitAt(4,4))


    @unittest.skip('Not needed')
    def test_grid_print(self):
        # arrange
        bb = BeverageBandidts()

        # act
        bb.load(test1)

        # assert
        bb.printGrid()

        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()

