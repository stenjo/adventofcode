# Test file for Advent of Code 2019: https://adventofcode.com/2019/day/10
#

import unittest
from AoC10_classes import AsteroidMap

class RunComputeTest(unittest.TestCase):

    def setUp(self):
        return super().setUp()

    def test_data_load_1(self):
        # arrange
        a = AsteroidMap()
        asteroids = ['.#..#','.....','#####','....#','...##']
        a.ReadMap(asteroids)

        # act
        c = a.count
        w = a.width
        result = a.GetBestLOS()

        # assert
        self.assertEqual(c, 10)
        self.assertEqual(w, 5)
        # self.assertEqual(result, (3,4))

    def test_data_load_2(self):
        # arrange
        a = AsteroidMap()
        asteroids = ['......#.#.','#..#.#....','..#######.','.#.#.###..','.#..#.....','..#....#.#','#..#....#.','.##.#..###','##...#..#.','.#....####']
        a.ReadMap(asteroids)

        # act
        c = a.count
        w = a.width
        result = a.GetBestLOS()

        # assert
        self.assertEqual(c, 40)
        self.assertEqual(w, 10)
        # self.assertEqual(result, (5,8))

    def test_data_load_3(self):
        # arrange
        a = AsteroidMap()
        asteroids = ['.#..#','.....','#####','....#','...##']
        a.ReadMap(asteroids)

        # act
        c = a.count
        w = a.width
        result = a.GetBestLOS()

        # assert
        self.assertEqual(c, 10)
        self.assertEqual(w, 5)
        # self.assertEqual(result, (3,4))

    def test_data_load_4(self):
        # arrange
        a = AsteroidMap()
        asteroids = ['.#..#','.....','#####','....#','...##']
        a.ReadMap(asteroids)

        # act
        c = a.count
        w = a.width
        result = a.GetBestLOS()

        # assert
        self.assertEqual(c, 10)
        self.assertEqual(w, 5)
        # self.assertEqual(result, (3,4))

    def test_LOS_blocking(self):
        # arrange
        a = AsteroidMap()
        asteroids = ['#.........','...A......','...B..a...','.EDCG....a','..F.c.b...','.....c....','..efd.c.gb','.......c..','....f...c.','...e..d..c']
        a.ReadMap(asteroids)
        check = [(3,1), (3,2), (6,2), (2,4), (2,6), (3,6), (4,6)]
        result = []
        revers = []

        # act
        for ast in check:
            result.append(a.IsLineOfSight((0,0), ast))
            revers.append(a.IsLineOfSight(ast, (0,0)))

        # assert
        self.assertEqual(result, [True, True, False, True, False, False, False])


    def test_best_view_1(self):
        # arrange
        a = AsteroidMap()
        asteroids = ['.#..#','.....','#####','....#','...##']
        a.ReadMap(asteroids)

        # act
        c = a.count
        w = a.width
        result = a.GetBestLOS()

        # assert
        self.assertEqual(c, 10)
        self.assertEqual(w, 5)
        # self.assertEqual(result, (3,4))


