# Test file for Advent of Code 2019: https://adventofcode.com/2019/day/18

import unittest
from AoC18_classes import Labyrinth



class TestLabyrinth(unittest.TestCase):

    def setUp(self):
        return super().setUp()

    def test_print_labyrinth(self):
        # arrange
        labMap = [
            '########################',
            '#f.D.E.e.C.b.A.@.a.B.c.#',
            '######################.#',
            '#d.....................#',
            '########################']
        l = Labyrinth(labMap)

        # act

        l.PrintMap()
        keyList = l.keys
        numKeys = len(keyList)
        doorsList = l.doors
        numDoors = len(doorsList)


        # assert
        print(list(keyList))
        print(list(doorsList))
        self.assertEqual(numKeys, 6)
        self.assertEqual(numDoors, 5)

    def test_full_labyrinth(self):
        # arrange
        infile = open('data/input_18.txt','r')
        labMap = infile.readlines()
        l = Labyrinth(labMap)

        # act

        l.PrintMap()
        keyList = l.GetKeys()
        numKeys = len(keyList)
        doorsList = l.GetDoors()
        numDoors = len(doorsList)


        # assert
        print(list(keyList))
        print(list(doorsList))
        self.assertEqual(numKeys, 26)
        self.assertEqual(numDoors, 26)

    def test_get_steps(self):
        # arrange
        labMap = [
            '########################',
            '#f.D.E.e.C.b.A.@.a.B.c.#',
            '######################.#',
            '#d.....................#',
            '########################']
        l = Labyrinth(labMap)
        steps = 30
        # act

        result = l.GetSteps('d')

        # assert
        self.assertEqual(result, steps)


    def test_get_doors(self):
        # arrange
        labMap = [
            '#################',
            '#i.G..c...e..H.p#',
            '########.########',
            '#j.A..b...f..D.o#',
            '########@########',
            '#k.E..a...g..B.n#',
            '########.########',
            '#l.F..d...h..C.m#',
            '#################']
        l = Labyrinth(labMap)

        # act
        doorsList = l.doors
        numDoors = len(doorsList)
        print(list(doorsList))
        print(l.MappedDoors())

        doorsNum = len(l.MappedDoors())

        # assert
        self.assertEqual(numDoors, doorsNum)