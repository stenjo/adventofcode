# Test file for Advent of Code 2019: https://adventofcode.com/2019/day/12

import unittest
from functools import reduce 
from AoC14_classes import NanoFactory

class NanoFactoryTest(unittest.TestCase):

    def setUp(self):
        return super().setUp()

    def test_example_1(self):
        # arrange
        reactions = [
            '10 ORE => 10 A',
            '1 ORE => 1 B',
            '7 A, 1 B => 1 C',
            '7 A, 1 C => 1 D',
            '7 A, 1 D => 1 E',
            '7 A, 1 E => 1 FUEL']
        nf = NanoFactory(reactions)

        # act
        result = nf.CalculateOre(1, 'FUEL')

        # assert
        self.assertEqual(result, 31 )
    
    def test_example_2(self):
        # arrange
        reactions = [
            '9 ORE => 2 A',
            '8 ORE => 3 B',
            '7 ORE => 5 C',
            '3 A, 4 B => 1 AB',
            '5 B, 7 C => 1 BC',
            '4 C, 1 A => 1 CA',
            '2 AB, 3 BC, 4 CA => 1 FUEL']

        nf = NanoFactory(reactions)

        # act
        result = nf.CalculateOre(1, 'FUEL')

        # assert
        self.assertEqual(result, 165)
    
    def test_dict_addition(self):
        # arrange
        reactions = ['10 ORE => 10 A','1 ORE => 1 B','7 A, 1 B => 1 C','7 A, 1 C => 1 D','7 A, 1 D => 1 E','7 A, 1 E => 1 FUEL']
        a = {'S': 1, 'T': 3, 'G':-2333}
        b = {'F': 0, 'T':-3, 'G': 2334}

        nf = NanoFactory(reactions)

        # act
        result = nf._add_dicts(a,b)

        # assert
        self.assertEqual(result, {'S': 1, 'T': 0, 'G':1, 'F': 0})

    def test_split_reaction(self):
        # arrange
        reaction = '5 B, 7 C => 1 BC'
        nf = NanoFactory([reaction])

        # act
        c, a, arr = nf.SplitReaction(reaction)

        # assert
        self.assertEqual(c, 'BC')
        self.assertEqual(a, 1)
        self.assertEqual(len(arr), 2)
        self.assertEqual(arr['B'], 5)
        self.assertEqual(arr['C'], 7)

    def test_split_reaction1(self):
        # arrange
        reaction = '2 AB, 3 BC, 4 CA => 1 FUEL'
        nf = NanoFactory([reaction])

        # act
        c, a, arr = nf.SplitReaction(reaction)

        # assert
        self.assertEqual(c, 'FUEL')
        self.assertEqual(a, 1)
        self.assertEqual(len(arr), 3)
        self.assertEqual(arr['AB'], 2)
        self.assertEqual(arr['BC'], 3)
        self.assertEqual(arr['CA'], 4)

    def test_split_reaction2(self):
        # arrange
        reaction = '9 ORE => 2 A'
        nf = NanoFactory([reaction])

        # act
        c, a, arr = nf.SplitReaction(reaction)

        # assert
        self.assertEqual(c, 'A')
        self.assertEqual(a, 2)
        self.assertEqual(len(arr), 1)
        self.assertEqual(arr['ORE'], 9)

    def test_split_reaction3(self):
        # arrange
        reaction = '44 XJWVT, 5 KHKGT, 1 QDVJ, 29 NZVS, 9 GPVTF, 48 HKGWZ => 1 FUEL'
        nf = NanoFactory([reaction])

        # act
        c, a, arr = nf.SplitReaction(reaction)

        # assert
        self.assertEqual(c, 'FUEL')
        self.assertEqual(a, 1)
        self.assertEqual(len(arr), 6)
        self.assertEqual(arr['XJWVT'], 44)
        self.assertEqual(arr['KHKGT'], 5)
        self.assertEqual(arr['QDVJ'], 1)
        self.assertEqual(arr['NZVS'], 29)
        self.assertEqual(arr['GPVTF'], 9)
        self.assertEqual(arr['HKGWZ'], 48)


if __name__ == '__main__':
    unittest.main()
