# Advent of Code 2019: https://adventofcode.com/2019/day/2
# 
# 
import math

class Compute():

    program = []
    
    def __init__(self, data):
        self.program = list(map(int, data))

    def RunCompute(self):
        index = 0
        while self.program[index] != 99:
            opcode = self.program[index]
            posval1 = self.program[index+1]
            posval2 = self.program[index+2]
            dest = self.program[index+3]

            if opcode == 1:
                self.program[dest] = self.program[posval1] + self.program[posval2]
            elif opcode == 2:
                self.program[dest] = self.program[posval1] * self.program[posval2]
            index += 4

        return self.program

    def Restore(self):
        self.program[1] = 12
        self.program[2] = 2
        return self.program

    def FindNounAndVerb(self, inputdata):
        noun = 0
        verb = 0
        for noun in range(100):
            for verb in range(100):
                self.program = list(map(int, inputdata))
                self.program[1] = noun
                self.program[2] = verb
                result = self.RunCompute()
                if result[0] == 19690720:
                    return 100 * noun + verb
