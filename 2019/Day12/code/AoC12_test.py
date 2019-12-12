#Test file for Advent of Code 2019: https://adventofcode.com/2019/day/12

import unittest
from AoC12_classes import Moon, MoonMap

class MoonTest(unittest.TestCase):

    def setUp(self):
        return super().setUp()

    def test_potential_energy(self):
        # arrange
        m = Moon('Moon', 99, -99, 0)

        # act
        result = m.PotentialEnergy()

        # assert
        self.assertEqual(result, 198)
    
    def test_load_moon(self):
        # arrange
        testInput = '<x=2, y=-10, z=-7>'
        m = Moon('Europa')

        # act
        m.LoadMoon(testInput)
        pe = m.PotentialEnergy()
        ke = m.KineticEnergy()

        # assert
        self.assertEqual(pe, 19)
        self.assertEqual(ke, 0)
    

    def test_load_moons(self):
        # arrange
        testInput = [
            '<x=-1, y=0, z=2>',
            '<x=2, y=-10, z=-7>',
            '<x=4, y=-8, z=8>',
            '<x=3, y=5, z=-1>']

        w = MoonMap(testInput)
        result = []

        # act
        for m in w.map:
            result.append(m.PotentialEnergy())

        # assert
        self.assertEqual(result, [3, 19, 20, 9])

    def test_move_moons(self):
        # arrange
        testInput = [
            '<x=-1, y=0, z=2>',
            '<x=2, y=-10, z=-7>',
            '<x=4, y=-8, z=8>',
            '<x=3, y=5, z=-1>']
        shouldBe = [(0, 1, 3), (3,-9,-6), (5, -7, 9), (4, 6, 0)]
        result = []

        w = MoonMap(testInput)
        for m in w.map:
            m.SetVelocity('<x=1, y=1, z=1>')

        # act
        for m in w.map:
            m.Move()
            result.append((m.pos['x'],m.pos['y'],m.pos['z']))

        # assert
        self.assertEqual(result, shouldBe)

    def test_one_step(self):
        # arrange
        testInput = [
            '<x=-1, y=0, z=2>',
            '<x=2, y=-10, z=-7>',
            '<x=4, y=-8, z=8>',
            '<x=3, y=5, z=-1>']
        shouldBe = [(0, 1, 3), (3,-9,-6), (5, -7, 9), (4, 6, 0)]
        pos = []
        vel = []

        w = MoonMap(testInput)

        # act
        w.OneStep()

        for m in w.map:
            pos.append(m.GetXYZAsTuple(m.pos))
            vel.append(m.GetXYZAsTuple(m.vel))

        # assert
        self.assertEqual(result, shouldBe)


    def test_load_moons_string(self):
        # arrange
        infile = open('data/input_12.txt','r')
        testInput = infile.readlines()
        w = MoonMap(testInput)
        result = []

        # act
        for p in range(25):
            result.append(w.GetPixelAt(p))

        # assert
        self.assertEqual(result, answer)


if __name__ == '__main__':
    unittest.main()
