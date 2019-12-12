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


    
class MoonMapTest(unittest.TestCase):

    def setUp(self):
        return super().setUp()

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
            result.append(m.AsTuple()[0])

        # assert
        self.assertEqual(result, shouldBe)

    def test_gravitate_moons(self):
        # arrange
        a = Moon(Name='Io',     pos='<x=-1, y=  0, z= 2>')
        b = Moon(Name='Europa', pos='<x= 2, y=-10, z=-7>')
        aShouldBe = (1,-1,-1) 
        bShouldBe = (-1,1,1) 
        mm = MoonMap()

        # act
        mm.Gravitate(a,b)

        # assert
        self.assertEqual(a.AsTuple()[1], aShouldBe)
        self.assertEqual(b.AsTuple()[1], bShouldBe)

    def test_step_10(self):
        # arrange
        testInput = [
            '<x=-1, y=0, z=2>',
            '<x=2, y=-10, z=-7>',
            '<x=4, y=-8, z=8>',
            '<x=3, y=5, z=-1>']
        shouldBe10 = [
            'pos=<x= 2, y= 1, z=-3>, vel=<x=-3, y=-2, z= 1>',
            'pos=<x= 1, y=-8, z= 0>, vel=<x=-1, y= 1, z= 3>',
            'pos=<x= 3, y=-6, z= 1>, vel=<x= 3, y= 2, z=-3>',
            'pos=<x= 2, y= 0, z= 4>, vel=<x= 1, y=-1, z=-1>']

        posShouldBe10 = [(2, 1, -3), (1, -8, 0), (3, -6, 1), (2, 0, 4)]
        velShouldBe10 = [(-3, -2, 1), (-1, 1, 3), (3, 2, -3), (1, -1, -1)]
        pos = []
        vel = []
        m = Moon()
        w = MoonMap(testInput)
        pos = []
        vel = []

        # act
        for i in range(10):
            w.OneStep()

        for m in w.map:
            pos.append(m.GetXYZAsTuple(m.pos))
            vel.append(m.GetXYZAsTuple(m.vel))
        
        # assert
        self.assertEqual(pos, posShouldBe10)
        self.assertEqual(vel, velShouldBe10)

    def test_step_0(self):
        # arrange
        testInput = [
            '<x=-1, y=0, z=2>',
            '<x=2, y=-10, z=-7>',
            '<x=4, y=-8, z=8>',
            '<x=3, y=5, z=-1>']
        shouldBe0 = [
            'pos=<x=-1, y=  0, z= 2>, vel=<x= 0, y= 0, z= 0>',
            'pos=<x= 2, y=-10, z=-7>, vel=<x= 0, y= 0, z= 0>',
            'pos=<x= 4, y= -8, z= 8>, vel=<x= 0, y= 0, z= 0>',
            'pos=<x= 3, y=  5, z=-1>, vel=<x= 0, y= 0, z= 0> ']

        posShouldBe0 = [(-1, 0, 2), (2, -10, -7), (4, -8, 8), (3, 5, -1)]
        velShouldBe0 = [(0, 0, 0), (0, 0, 0), (0, 0, 0), (0, 0, 0)]

        w = MoonMap(testInput)
        pos = []
        vel = []

        # act
        # w.OneStep()

        for m in w.map:
            pos.append(m.GetXYZAsTuple(m.pos))
            vel.append(m.GetXYZAsTuple(m.vel))
        
        # assert
        self.assertEqual(pos, posShouldBe0)
        self.assertEqual(vel, velShouldBe0)

    def test_step_1(self):
        # arrange
        testInput = [
            '<x=-1, y=0, z=2>',
            '<x=2, y=-10, z=-7>',
            '<x=4, y=-8, z=8>',
            '<x=3, y=5, z=-1>']
        shouldBe1 = [
            'pos=<x= 2, y=-1, z= 1>, vel=<x= 3, y=-1, z=-1>',
            'pos=<x= 3, y=-7, z=-4>, vel=<x= 1, y= 3, z= 3>',
            'pos=<x= 1, y=-7, z= 5>, vel=<x=-3, y= 1, z=-3>',
            'pos=<x= 2, y= 2, z= 0>, vel=<x=-1, y=-3, z= 1>']

        posShouldBe1 = [(2, -1, 1), (3, -7, -4), (1, -7, 5), (2, 2, 0)]
        velShouldBe1 = [(3, -1, -1), (1, 3, 3), (-3, 1, -3), (-1, -3, 1)]
        pos = []
        vel = []

        w = MoonMap(testInput)

        # act
        w.OneStep()

        for m in w.map:
            pos.append(m.GetXYZAsTuple(m.pos))
            vel.append(m.GetXYZAsTuple(m.vel))
        
        # assert
        self.assertEqual(vel, velShouldBe1)
        self.assertEqual(pos, posShouldBe1)

    def test_step_2(self):
        # arrange
        testInput = [
            '<x=-1, y=0, z=2>',
            '<x=2, y=-10, z=-7>',
            '<x=4, y=-8, z=8>',
            '<x=3, y=5, z=-1>']
        shouldBe2 = [
            'pos=<x= 5, y=-3, z=-1>, vel=<x= 3, y=-2, z=-2>','pos=<x= 1, y=-2, z= 2>, vel=<x=-2, y= 5, z= 6>','pos=<x= 1, y=-4, z=-1>, vel=<x= 0, y= 3, z=-6>','pos=<x= 1, y=-4, z= 2>, vel=<x=-1, y=-6, z= 2>']

        posShouldBe2 = [(5, -3, -1), (1, -2, 2), (1, -4, -1), (1, -4, 2)]
        velShouldBe2 = [(3, -2, -2), (-2, 5, 6), (0, 3, -6), (-1, -6, 2)]
        pos = []
        vel = []
        m = Moon()
        for l in shouldBe2:
            p,v = m.GetPosAndVelFromString(l)
            pos.append(p)
            vel.append(v)
        print(pos)
        print(vel)

        w = MoonMap(testInput)
        pos = []
        vel = []

        # act
        w.OneStep()
        w.OneStep()

        for m in w.map:
            pos.append(m.GetXYZAsTuple(m.pos))
            vel.append(m.GetXYZAsTuple(m.vel))
        
        # assert
        self.assertEqual(pos, posShouldBe2)
        self.assertEqual(vel, velShouldBe2)

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

    def test_total_energy_1(self):
                # arrange
        testInput = [
            '<x=-1, y=0, z=2>',
            '<x=2, y=-10, z=-7>',
            '<x=4, y=-8, z=8>',
            '<x=3, y=5, z=-1>']

        w = MoonMap(testInput)
        # act
        for i in range(10):
            w.OneStep()

        t = w.TotalEnergy()

        # assert
        self.assertEqual(t, 179)

    def test_total_energy_2(self):
        # arrange
        testInput = [
            '<x=-8, y=-10, z=0>',
            '<x=5, y=5, z=10>',
            '<x=2, y=-7, z=3>',
            '<x=9, y=-8, z=-3>']

        w = MoonMap(testInput)
        # act
        for i in range(100):
            w.OneStep()

        t = w.TotalEnergy()

        # assert
        self.assertEqual(t, 1940)

    def test_moves_to_origin_1(self):
        # arrange
        testInput = [
            '<x=-1, y=0, z=2>',
            '<x=2, y=-10, z=-7>',
            '<x=4, y=-8, z=8>',
            '<x=3, y=5, z=-1>']

        w = MoonMap(testInput)
        # act
        moves = 1
        w.OneStep()
        while w.AllWasAtOriginalPos() == False:
            w.OneStep()
            moves += 1
        
        print([m.loopSteps for m in w.map])

        # assert
        self.assertEqual(moves, 2772)

    def test_moves_to_origin_2(self):
        # arrange
        testInput = [
            '<x=-8, y=-10, z=0>',
            '<x=5, y=5, z=10>',
            '<x=2, y=-7, z=3>',
            '<x=9, y=-8, z=-3>']

        w = MoonMap(testInput)
        # act
        moves = 1
        w.OneStep()
        # while w.AllAtOriginalPos() == False:
        while w.AllWasAtOriginalPos() == False:
            w.OneStep()
            moves += 1
            if moves % 100 == 0:
                print([m.loopSteps for m in w.map])

        # assert
        self.assertEqual(moves, 4686774924)

    def test_moves_to_origin_puzle(self):
        # arrange
        infile = open('data/input_12.txt','r')
        testInput = infile.readlines()

        w = MoonMap(testInput)
        # act
        moves = 1
        w.OneStep()
        # while w.AllAtOriginalPos() == False:
        while w.AllWasAtOriginalPos() == False:
            w.OneStep()
            moves += 1
            if moves % 1000 == 0:
                print([m.loopStepsXYZ for m in w.map])

        # assert
        self.assertEqual(moves, 4686774924)


if __name__ == '__main__':
    unittest.main()
