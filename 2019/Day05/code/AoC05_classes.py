# Advent of Code 2019: https://adventofcode.com/2019/day/5
# 
# 
import math

class Compute():

    program = []
    inputList = []
    outputList = []

    def __init__(self, data):
        self.LoadProgram(data)

    def LoadInput(self, data):
        self.inputList = []
        for n in data:
            self.inputList.append(n)
        self.inputList.reverse()

    def LoadProgram(self, data):
        self.program = list(map(int, data))
    
    def AddToOutput(self, data):
        self.outputList.append(data)

    def GetNextInput(self):
        if len(self.inputList) > 0:
            return self.inputList.pop()
        else:
            print('Index input too large:', self.outputList)
        

    def RunCompute(self):
        index = 0
        self.outputList = []
        while self.program[index] != 99:
            modes = self.program[index] // 100
            mode1 = modes % 10
            mode2 = modes // 10 % 10
            mode3 = modes // 100 % 10

            opcode = self.program[index] % 100

            posval1 = self.program[index+1]
            val1 = posval1 if mode1 == 1 else self.program[posval1]

            posval2 = None
            val2 = None
            if index+2 < len(self.program):
                posval2 = self.program[index+2]
                val2 = posval2 
                if mode2 == 0 and posval2 < len(self.program):
                    val2 = self.program[posval2]

            dest = None
            if index + 3 < len(self.program):
                dest = self.program[index+3]


            if opcode == 1:
                self.program[dest] = val1 + val2
                # print(index, ':  ','Op:', opcode, '  ', mode1, ':', val1, '  ', mode2, ':', val2, ' Add: ', val1, '+', val2, 'and save into', dest)
                index += 4

            elif opcode == 2:
                self.program[dest] = val1 * val2
                # print(index, ':  ','Op:', opcode, '  ', mode1, ':', val1, '  ', mode2, ':', val2)
                index += 4

            elif opcode == 3:
                self.program[posval1] = self.GetNextInput()
                # print(index, ':  ','Op:', opcode, '  ', mode1, ':', posval1, '  ', ' Load input: ', self.program[posval1], 'and save into', posval1)
                index += 2

            elif opcode == 4:
                self.AddToOutput(val1)
                # print(index, ':  ','Op:', opcode, '  ', mode1, ':', val1, '  ', ' Write output: ', val1)
                index += 2

            elif opcode == 5:
                # print(index, ':  ','Op:', opcode, '  ', mode1, ':', val1, '  ', mode2, ':', val2, ' Jump if true: ', val1, '!= 0 -> jump to', val2)
                index = val2 if val1 != 0 else index + 3

            elif opcode == 6:
                # print(index, ':  ','Op:', opcode, '  ', mode1, ':', val1, '  ', mode2, ':', val2, ' Jump if false: ', val1, '== 0 -> jump to', val2)
                index = val2 if val1 == 0 else index + 3

            elif opcode == 7:
                self.program[dest] = 1 if val1 < val2 else 0
                # print(index, ':  ','Op:', opcode, '  ', mode1, ':', val1, '  ', mode2, ':', val2, ' Less than: ', val1, '=', val2, ' wrote ', self.program[dest], ' into ', dest)
                index += 4

            elif opcode == 8:
                self.program[dest] = 1 if val1 == val2 else  0
                # print(index, ':  ','Op:', opcode, '  ', mode1, ':', val1, '  ', mode2, ':', val2, ' Equals: ', val1, '=', val2, ' wrote ', self.program[dest], ' into ', dest)
                index += 4
            else:
                # print(index, ':  ','Op:', opcode, '  ', mode1, ':', val1)
                return self.outputList

            if mode3 == 1:
                print(index, ':  ','Op:', opcode, '  ', mode1, ':', val1, '  ', mode2, ':', val2, '  ', mode3, ':', dest)

            # print(self.program)

            # self.outputList.reverse()
        if len(self.outputList) > 0 :
            return self.outputList[-1] 
        else: 
            return self.program[index]

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

