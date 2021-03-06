# Test file for Advent of Code 2019: https://adventofcode.com/2019/day/23

import unittest
import pprint as pp
from AoC23_classes import NetworkInterfaceController, Compute



class NetworkInterfaceControllerTest(unittest.TestCase):

    def setUp(self):
        return super().setUp()

    def test_run_code(self):
        # arrange
        infile = open('data/input_23.txt','r')
        program = infile.readline().strip().split(',')
        n = NetworkInterfaceController(program)

        # act
        numOutputs = n.RunComputers()

        # assert
        self.assertEqual(numOutputs, 23626 )

    def test_run_nat(self):
        # arrange
        infile = open('data/input_23.txt','r')
        program = infile.readline().strip().split(',')
        n = NetworkInterfaceController(program)

        # act
        numOutputs = n.RunForNAT()

        # assert
        self.assertEqual(numOutputs, 19021 )

    def test_run_computer(self):
        # arrange
        infile = open('data/input_23.txt','r')
        program = infile.readline().strip().split(',')
        n = NetworkInterfaceController(program)
        computer = n.computers[0]['c']

        # act
        n.RunComputer(0,computer)
        result = computer.GetOutputs()
        waiting = computer.WaitingForInput()

        # assert
        self.assertEqual(waiting, True)
        self.assertEqual(result, [] )
        


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

    def test_add_to_input(self):
        # arrange
        program = [104,1125899906842624,99]
        c = Compute(program)

        # act
        c.LoadInput([0])
        c.LoadProgram(program)
        c.AddToInput([1,2])
        result = list(c.inputList)
        result.reverse()

        # assert
        self.assertEqual(result, [0, 1, 2])