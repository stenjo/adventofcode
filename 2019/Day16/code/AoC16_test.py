# Test file for Advent of Code 2019: https://adventofcode.com/2019/day/16

import unittest
from AoC16_classes import Pattern, FFT


class Signal(unittest.TestCase):

    def setUp(self):
        return super().setUp()

    def test_signal_1(self):
        # arrange
        signal = '12345678'
        pattern = [0, 1, 0, -1]
        s = FFT(pattern, signal)

        # act
        result = s.RunPhase(4)

        # assert
        self.assertEqual(result, '01029498' )

    def test_signal_2(self):
        # arrange
        signal = '80871224585914546619083218645595'
        pattern = [0, 1, 0, -1]
        s = FFT(pattern, signal)

        # act
        result = s.RunPhase(100)

        # assert
        self.assertEqual(result, '24176176' )

    def test_signal_3(self):
        # arrange
        signal = '19617804207202209144916044189917'
        pattern = [0, 1, 0, -1]
        s = FFT(pattern, signal)

        # act
        result = s.RunPhase(100)

        # assert
        self.assertEqual(result, '73745418' )

    def test_signal_4(self):
        # arrange
        signal = '69317163492948606335995924319873'
        pattern = [0, 1, 0, -1]
        s = FFT(pattern, signal)

        # act
        result = s.RunPhase(100)

        # assert
        self.assertEqual(result, '52432133' )

    def test_with_offset_1(self):
        # arrange
        signal = '123456781234567812345678123456781234567812345678'
        multiplier = 6
        pattern = [0, 1, 0, -1]
        s = FFT(pattern, signal)

        # act
        # 1846033423791261356214140202763688249498
        result = s.RunPhase(4,24)
        result = s.RunPhaseWithOffset(4,8)

        # assert
        self.assertEqual(result, '35621414' )

