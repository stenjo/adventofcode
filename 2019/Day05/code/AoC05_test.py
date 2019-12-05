#Test file for Advent of Code Day 3

import unittest
from AoC05_classes import Compute

class RunComputeTest(unittest.TestCase):

    def setUp(self):
        return super().setUp()

    def test_compute_mode_1(self):
        # arrange
        testInput = [1002,4,3,4,33]
        w = Compute(testInput)

        # act
        result = w.RunCompute()

        # assert
        self.assertEqual(result, 99)
    
    def test_compute_mode_2(self):
        # arrange
        testInput = [1101,100,-1,4,0]
        w = Compute(testInput)

        # act
        result = w.RunCompute()

        # assert
        self.assertEqual(result, 99)

    def test_opcode_less_than_8_pos(self):
        # arrange
        program = [3,9,7,9,10,9,4,9,99,-1,8]
        testvalues = [7,8,9]
        results = []
        c = Compute(program)

        # act
        for v in testvalues:
            c.LoadInput([v])
            results.append(c.RunCompute())

        # assert
        self.assertEqual(results, [1,0,0])

    def test_opcode_lequal_to_8_pos(self):
        # arrange
        program = [3,9,8,9,10,9,4,9,99,-1,8]
        testvalues = [7,8,9]
        results = []
        c = Compute(program)

        # act
        for v in testvalues:
            c.LoadInput([v])
            results.append(c.RunCompute())

        # assert
        self.assertEqual(results, [0,1,0])

    def test_opcode_less_than_8(self):
        # arrange
        program = [3,3,1107,-1,8,3,4,3,99]
        testvalues = [7,8,9]
        results = []
        c = Compute(program)

        # act
        for v in testvalues:
            c.LoadInput([v])
            results.append(c.RunCompute())

        # assert
        self.assertEqual(results, [1,0,0])

    def test_opcode_lequal_to_8(self):
        # arrange
        program = [3,3,1108,-1,8,3,4,3,99]
        testvalues = [7,8,9]
        results = []
        c = Compute(program)

        # act
        for v in testvalues:
            c.LoadInput([v])
            results.append(c.RunCompute())

        # assert
        self.assertEqual(results, [0,1,0])

    def test_large_example(self):
        # arrange
        program = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
        testvalues = [7,8,9]
        results = []
        c = Compute(program)

        # act
        for v in testvalues:
            c.LoadInput([v])
            results.append(c.RunCompute())

        # assert
        self.assertEqual(results, [999,1000,1001])

    def test_jump_position(self):
        # arrange
        program = [3,12,6,12,15,1,13,14,13,4,13,99,-1,0,1,9]
        testvalues = [1,-8,0]
        results = []
        c = Compute(program)

        # act
        for v in testvalues:
            c.LoadInput([v])
            results.append(c.RunCompute())

        # assert
        self.assertEqual(results, [1,1,0])

    def test_jump_immediate(self):
        # arrange
        program = [3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
        testvalues = [0,1,-9]
        results = []
        c = Compute(program)

        # act
        for v in testvalues:
            c.LoadInput([v])
            results.append(c.RunCompute())
            print(c.GetOutputs())

        # assert
        self.assertEqual(results, [0,1,1])

if __name__ == '__main__':
    unittest.main()
