# Test file for Advent of Code 2019: https://adventofcode.com/2019/day/21

import unittest
import pprint as pp
from AoC21_classes import SpringDroid, Compute



class SpringDroidMap(unittest.TestCase):

    def setUp(self):
        return super().setUp()

    def test_run_code(self):
        # arrange
        infile = open('data/input_21.txt','r')
        program = infile.readline().strip().split(',')
        c = Compute(program)
        s = []

        # act
        s = c.RunForNewline()
        print(s)
        print(''.join([chr(a) for a in s]))

        # assert
        self.assertEqual(True, True)

    def test_small_program(self):
        # arrange
        instr = [
            'NOT A J',
            'NOT B T',
            'AND T J',
            'NOT C T',
            'AND T J',
            'AND D J',
            'WALK']

        s = []

        sd = SpringDroid()
        s = sd.RunProgram()
        sd.LoadAsciiProgram(instr)
        result = []

        # act
        for i in range(len(instr)+60):
            s = sd.RunProgram()
            result.append(s)
            print(s, end = '')
            # print(''.join([chr(a) for a in s]))

        # pp.pprint(result)

        # assert
        self.assertEqual(True, True)

    def test_small_program_1(self):
        # arrange
        instr = [
            'NOT D T',
            'AND A T',
            'AND B T',
            'AND C T',
            'OR T J',
            'NOT C J',
            'WALK']

        s = []

        sd = SpringDroid()
        s = sd.RunProgram()
        sd.LoadAsciiProgram(instr)
        result = []

        # act
        for i in range(len(instr)+60):
            s = sd.RunProgram()
            result.append(s)
            print(s, end = '')

        # assert
        self.assertEqual(True, True)




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
            c.LoadProgram(program)
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
            c.LoadProgram(program)
            results.append(c.RunCompute())
            # print(c.GetOutputs())

        # assert
        self.assertEqual(results, [0,1,1])

    def test_rel_base_offset_1(self):
        # arrange
        program = [109,1,204,-1,1001,100,1,100,1008,100,16,101,1006,101,0,99]
        results = []
        c = Compute(program)

        # act
        c.LoadInput([])
        c.RunCompute()
        results=c.GetOutputs()

        # assert
        self.assertEqual(results, program)

    def test_rel_base_offset_2(self):
        # arrange
        program = [1102,34915192,34915192,7,4,7,99,0]
        results = []
        c = Compute(program)

        # act
        c.LoadInput([])
        c.LoadProgram(program)
        output=c.RunCompute()
        result = len([int(d) for d in str(output)])

        # assert
        self.assertEqual(result, 16)

    def test_rel_base_offset_3(self):
        # arrange
        program = [104,1125899906842624,99]
        c = Compute(program)

        # act
        c.LoadInput([])
        c.LoadProgram(program)
        result = c.RunCompute()

        # assert
        self.assertEqual(result, 1125899906842624)

