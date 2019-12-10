# Test file for Advent of Code 2019: https://adventofcode.com/2019/day/10
#

import unittest
from pprint import pprint
from AoC10_classes import AsteroidMap

class RunComputeTest(unittest.TestCase):

    def setUp(self):
        return super().setUp()

    def test_data_load_1(self):
        # arrange
        a = AsteroidMap()
        asteroids = [
            '.#..#',
            '.....',
            '#####',
            '....#',
            '...##']
        a.ReadMap(asteroids)

        # act
        c = a.count
        w = a.width
        result = a.GetBestLOS()

        a.PrintAsteroids()

        # assert
        self.assertEqual(c, 10)
        self.assertEqual(w, 5)
        self.assertEqual(result, (3,4))

    def test_data_load_2(self):
        # arrange
        a = AsteroidMap()
        asteroids = [
            '......#.#.',
            '#..#.#....',
            '..#######.',
            '.#.#.###..',
            '.#..#.....',
            '..#....#.#',
            '#..#....#.',
            '.##.#..###',
            '##...#..#.',
            '.#....####']
        a.ReadMap(asteroids)

        # act
        c = a.count
        w = a.width
        result = a.GetBestLOS()

        # assert
        self.assertEqual(c, 40)
        self.assertEqual(w, 10)
        self.assertEqual(result, (5,8))
        self.assertEqual(a.astDict[result]['sees'], 33)

    def test_data_load_3(self):
        # arrange
        a = AsteroidMap()
        asteroids = [
            '#.#...#.#.',
            '.###....#.',
            '.#....#...',
            '##.#.#.#.#',
            '....#.#.#.',
            '.##..###.#',
            '..#...##..',
            '..##....##',
            '......#...',
            '.####.###.']
        a.ReadMap(asteroids)

        # act
        c = a.count
        w = a.width
        result = a.GetBestLOS()

        # assert
        self.assertEqual(c, 40)
        self.assertEqual(w, 10)
        self.assertEqual(result, (1,2))
        self.assertEqual(a.astDict[result]['sees'], 35)

    def test_data_load_4(self):
        # arrange
        a = AsteroidMap()
        asteroids = [
            '.#..#..###',
            '####.###.#',
            '....###.#.',
            '..###.##.#',
            '##.##.#.#.',
            '....###..#',
            '..#.#..#.#',
            '#..#.#.###',
            '.##...##.#',
            '.....#.#..']
        a.ReadMap(asteroids)

        # act
        c = a.count
        w = a.width
        result = a.GetBestLOS()

        # assert
        self.assertEqual(c, 50)
        self.assertEqual(w, 10)
        self.assertEqual(result, (6,3))
        self.assertEqual(a.astDict[result]['sees'], 41)

    def test_data_load_5(self):
        # arrange
        a = AsteroidMap()
        asteroids = [
            '.#..##.###...#######',
            '##.############..##.',
            '.#.######.########.#',
            '.###.#######.####.#.',
            '#####.##.#.##.###.##',
            '..#####..#.#########',
            '####################',
            '#.####....###.#.#.##',
            '##.#################',
            '#####.##.###..####..',
            '..######..##.#######',
            '####.##.####...##..#',
            '.#####..#.######.###',
            '##...#.##########...',
            '#.##########.#######',
            '.####.#.###.###.#.##',
            '....##.##.###..#####',
            '.#.#.###########.###',
            '#.#.#.#####.####.###',
            '###.##.####.##.#..##']
        a.ReadMap(asteroids)

        # act
        c = a.count
        w = a.width
        result = a.GetBestLOS()

        a.PrintAsteroids()

        # assert
        self.assertEqual(c, 300)
        self.assertEqual(w, 20)
        self.assertEqual(result, (11,13))
        self.assertEqual(a.astDict[result]['sees'], 210)

    def test_LOS_blocking(self):
        # arrange
        a = AsteroidMap()
        asteroids = [
            '#........O',
            'O..A......',
            'O..B..a...',
            '.EDCG....a', #3
            '..F.c.b...', #4
            '.....c....', #5
            '..efd.c.gb', #6
            '.......c..', #7
            '....f...c.', #8
            '...e..d..c'] #9
           # 0123456789
        a.ReadMap(asteroids)
        indata  = [(3,1), (3,2), (6,2), (2,4), (2,6), (3,6), (4,6), (0,2), (6,2), (9,9), (2,3), 
        (3,3), (4,3), (5,3), (6,6), (8,6), (9,6), (7,7), (4,8), (8,8), (3,9), (6,9), (9,0), (0,1),
        (1,3)]
        correct = [ True,  True, False,  True, False, False, False, False, False, False,  True,  
         True,  True,  True, False, False, False, False, False, False, False, False,  True,  True,
         True]
        result = []
        revers = []

        # act
        for ast in indata:
            result.append(a.IsLineOfSight((0,0), ast))
            revers.append(a.IsLineOfSight(ast, (0,0)))

        # pprint(a.astDict)

        # assert
        self.assertEqual(result, correct)
        self.assertEqual(revers, correct)


    def test_best_view_1(self):
        # arrange
        a = AsteroidMap()
        asteroids = [
            '.#..#',
            '.....',
            '#####',
            '....#',
            '...##']
        a.ReadMap(asteroids)
        # pprint(a.astDict)

        # act
        c = a.count
        w = a.width
        result = a.GetBestLOS()
        a.PrintAsteroids()

        # assert
        self.assertEqual(c, 10)
        self.assertEqual(w, 5)
        self.assertEqual(result, (3,4))

    def test_get_blocking(self):
        # arrange
        am = AsteroidMap()
        a = [(0,0), (0,4), (4,0), (0,4), (1,0), (3,0)]
        b = [(4,4), (4,0), (2,0), (0,4), (3,4), (1,4)]
        r = [
            [(1,1), (2,2), (3,3)], 
            [(3,1), (2,2), (1,3)], 
            [(3,0)], 
            [],
            [(2,2)],
            [(2,2)]
            ]
        l = []

        # act
        for i in range(len(a)):
            l.append(am.GetPositionsBetweenAsteroids(a[i], b[i]))

        # assert
        pprint(l)
        for n in range(len(r)):
            self.assertEqual(set(l[n]), set(r[n]))

