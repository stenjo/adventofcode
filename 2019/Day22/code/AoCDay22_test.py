# Test file for Advent of Code 2019, Day 22: 

import unittest
from AoCDay22_classes import SpaceDeck


class SpaceDeckTest(unittest.TestCase):

    def setUp(self):
        return super().setUp()

    def test_cut_n(self):
        # arrange
        d = SpaceDeck(10)

        # act
        result = d.CutN(3)

        # assert
        self.assertEqual(result, [3,4,5,6,7,8,9,0,1,2])

    def test_cut_n_1(self):
        # arrange
        d = SpaceDeck(10)

        # act
        result = d.CutN(7)

        # assert
        self.assertEqual(result, [7,8,9,0,1,2,3,4,5,6])

    def test_cut_n_2(self):
        # arrange
        d = SpaceDeck(10)

        # act
        result = d.CutN(7)

        # assert
        self.assertEqual(result, [7,8,9,0,1,2,3,4,5,6])

    def test_cut_n_neg(self):
        # arrange
        d = SpaceDeck(6)

        # act
        result = d.CutN(-4)

        # assert
        self.assertEqual(result, [2,3,4,5,0,1])

    def test_cut_n_neg_1(self):
        # arrange
        d = SpaceDeck(10)

        # act
        result = d.CutN(-4)

        # assert
        self.assertEqual(result, [6,7,8,9,0,1,2,3,4,5])

    def test_deal_into_new(self):
        # arrange
        d = SpaceDeck(9)

        # act
        result = d.DealIntoNew()

        # assert

        self.assertEqual(result, [8,7,6,5,4,3,2,1,0])

    def test_deal_with_increment(self):
        # arrange
        d = SpaceDeck(7)

        # act
        result = d.DealWithIncrement(3)

        # asssert
        self.assertEqual(result, [0,5,3,1,6,4,2])

    def test_run_deal_1(self):
        # arrange
        d = SpaceDeck(10)
        deals = [
            'deal with increment 7',
            'deal into new stack',
            'deal into new stack']
        deck = '0 3 6 9 2 5 8 1 4 7'
        result = []

        # act
        result = d.RunDeal(deals)

        # assert
        self.assertEqual(' '.join([str(n) for n in result]), deck)

    def test_run_deal_2(self):
        # arrange
        d = SpaceDeck(10)
        deals = [
            'cut 6',
            'deal with increment 7',
            'deal into new stack']
        deck = '3 0 7 4 1 8 5 2 9 6'
        result = []

        # act
        result = d.RunDeal(deals)

        # assert
        self.assertEqual(' '.join([str(n) for n in result]), deck)

    def test_run_deal_3(self):
        # arrange
        d = SpaceDeck(10)
        deals = [
            'deal with increment 7',
            'deal with increment 9',
            'cut -2'
            ]
        deck = '6 3 0 7 4 1 8 5 2 9'
        result = []

        # act
        result = d.RunDeal(deals)

        # assert
        self.assertEqual(' '.join([str(n) for n in result]), deck)

    def test_run_deal_4(self):
        # arrange
        d = SpaceDeck(10)
        deals = [
            'deal into new stack',
            'cut -2',
            'deal with increment 7',
            'cut 8',
            'cut -4',
            'deal with increment 7',
            'cut 3',
            'deal with increment 9',
            'deal with increment 3',
            'cut -1'
            ]
        deck = '9 2 5 8 1 4 7 0 3 6'
        result = []

        # act
        result = d.RunDeal(deals)

        # assert
        self.assertEqual(' '.join([str(n) for n in result]), deck)

    def test_run_deal_actual(self):
        # arrange
        d = SpaceDeck(10007)
        infile = open('data/input_22.txt','r')
        deals = infile.readlines()
        answer = 5169
        result = []

        # act
        result = d.RunDeal(deals)

        # assert
        self.assertEqual(result.index(2019), answer)


    def test_run_deal_actual_1(self):
        # arrange
        d = SpaceDeck(10007)
        infile = open('data/input_22.txt','r')
        deals = infile.readlines()
        answer = 10006
        result = []

        # act
        result = d.RunDealUntilSorted(deals)

        # assert
        self.assertEqual(result, answer)

        