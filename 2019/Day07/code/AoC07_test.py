#Test file for Advent of Code 2019: https://adventofcode.com/2019/day/7

import unittest
from AoC07_classes import AmplificationCircuit, Amplifier, Compute

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

    def test_get_truster_1(self):
        # arrange
        program = [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0]
        phaseSequence = [4,3,2,1,0]
        a = AmplificationCircuit(0, program)

        # act
        result = a.RunPhaseSet(phaseSequence)

        # assert
        self.assertEqual(result, 43210)
    
    def test_get_truster_2(self):
        # arrange
        program = [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0]
        phaseSequence = [0,1,2,3,4]
        a = AmplificationCircuit(0, program)

        # act
        result = a.RunPhaseSet(phaseSequence)

        # assert
        self.assertEqual(result, 54321)
    
    def test_get_truster_3(self):
        # arrange
        program = [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
        phaseSequence = [1,0,4,3,2]
        a = AmplificationCircuit(0, program)

        # act
        result = a.RunPhaseSet(phaseSequence)

        # assert
        self.assertEqual(result, 65210)
    
    def test_amplify_0(self):

        # arrange

        # act

        # assert
        self.assertEqual(0, 0)

    def test_amplify_large(self):
        # arrange
        program = [3,21,1008,21,8,20,1005,20,22,107,8,21,20,1006,20,31,1106,0,36,98,0,0,1002,21,125,20,4,20,1105,1,46,104,999,1105,1,46,1101,1000,1,20,4,20,1105,1,46,98,99]
        testvalues = [7,8,9]
        results = []

        # act
        for v in testvalues:
            a = Amplifier(program)
            results.append(a.Amplify(v, 0))

        # assert
        self.assertEqual(results, [999,1000,1001])

    def test_set_generator(self):
        # arrange
        a = AmplificationCircuit(0,[99])

        # act
        sets = a.GetPhaseSets()

        # assert
        self.assertEqual(len(sets), 120)    # should be n!/(n-r)! combinations

    def test_loopbacktruster_1(self):
        # arrange
        program = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
        phaseSequence = [9,8,7,6,5]
        a = AmplificationCircuit(0, program)

        # act
        result = a.RunLoopbackPhaseSet(phaseSequence)

        # assert
        self.assertEqual(result[0], 139629729)
    
    def test_loopbacktruster_2(self):
        # arrange
        program = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,-5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
        phaseSequence = [9,7,8,5,6]
        a = AmplificationCircuit(0, program)

        # act
        result = a.RunLoopbackPhaseSet(phaseSequence)

        # assert
        self.assertEqual(result[0], 18216)


if __name__ == '__main__':
    unittest.main()
