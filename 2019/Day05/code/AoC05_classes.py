# Advent of Code 2019: https://adventofcode.com/2019/day/5
# 
# 
import math

class Compute():

    program = []
    inputList = []
    inputPos = 0
    outputList = []

    def __init__(self, data):
        self.program = list(map(int, data))
        # self.program.append('' * 4)

    def LoadInput(self, data):
        for n in data:
            self.inputList.append(n)
    
    def AddToOutput(self, data):
        self.outputList.append(data)

    def GetNextInput(self):
        if self.inputPos < len(self.inputList):
            val = self.inputList[self.inputPos]
            self.inputPos += 1
            return val
        else:
            print('Idex input too large:', self.outputList)
        

    def RunCompute(self):
        index = 0
        while self.program[index] != 99:
            modes = self.program[index] // 100
            mode1 = modes % 10
            mode2 = modes // 10 % 10
            mode3 = modes // 100 % 10

            opcode = self.program[index] % 100
            posval1 = self.program[index+1]

            val1 = posval1 if mode1 == 1 else self.program[posval1]


            if opcode == 1:
                posval2 = self.program[index+2]
                val2 = posval2 if mode2 == 1 else self.program[posval2]
                dest = self.program[index+3]
                self.program[dest] = val1 + val2
                index += 4
                print('Op:', opcode, '  ', mode1, ':', val1, '  ', mode2, ':', val2)
            elif opcode == 2:
                posval2 = self.program[index+2]
                val2 = posval2 if mode2 == 1 else self.program[posval2]
                dest = self.program[index+3]
                index += 4
                self.program[dest] = val1 * val2
                print('Op:', opcode, '  ', mode1, ':', val1, '  ', mode2, ':', val2)
            elif opcode == 3:
                self.program[posval1] = self.GetNextInput()
                index += 2
                print('Op:', opcode, '  ', mode1, ':', val1)
            elif opcode == 4:
                self.AddToOutput(posval1)
                index += 2
                print('Op:', opcode, '  ', mode1, ':', val1)
            else:
                return self.program

            
        return self.program

    def GetValueAt(self, index):
        return self.program[index]

    def GetOutputs(self):
        return self.outputList

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

