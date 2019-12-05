# Advent of Code 2019: https://adventofcode.com/2019/day/6
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

            arg1 = self.program[index+1]
            val1 = arg1 if mode1 == 1 else self.program[arg1]

            arg2 = self.program[index+2] if index+2 < len(self.program) else None
            val2 = self.program[arg2] if mode2 == 0 and arg2 < len(self.program) else arg2

            dest = self.program[index+3] if index + 3 < len(self.program) else None

            if opcode == 1:
                index = self.OpAdd(val1, val2, dest, index)
                # self.program[dest] = val1 + val2
                # print(index, ':  ','Op:', opcode, '  ', mode1, ':', val1, '  ', mode2, ':', val2, ' Add: ', val1, '+', val2, 'and save into', dest)
                # index += 4

            elif opcode == 2:
                index = self.OpMul(val1, val2, dest, index)
                # self.program[dest] = val1 * val2
                # print(index, ':  ','Op:', opcode, '  ', mode1, ':', val1, '  ', mode2, ':', val2)
                # index += 4

            elif opcode == 3:
                index = self.OpLoad(arg1, val2, dest, index)
                # self.program[arg1] = self.GetNextInput()
                # print(index, ':  ','Op:', opcode, '  ', mode1, ':', arg1, '  ', ' Load input: ', self.program[arg1], 'and save into', arg1)
                # index += 2

            elif opcode == 4:
                index = self.OpSave(val1, val2, dest, index)
                # self.AddToOutput(val1)
                # print(index, ':  ','Op:', opcode, '  ', mode1, ':', val1, '  ', ' Write output: ', val1)
                # index += 2

            elif opcode == 5:
                index = self.OpJumpOnTrue(val1, val2, dest, index)
                # print(index, ':  ','Op:', opcode, '  ', mode1, ':', val1, '  ', mode2, ':', val2, ' Jump if true: ', val1, '!= 0 -> jump to', val2)
                # index = val2 if val1 != 0 else index + 3

            elif opcode == 6:
                index = self.OpJumpOnFalse(val1, val2, dest, index)
                # print(index, ':  ','Op:', opcode, '  ', mode1, ':', val1, '  ', mode2, ':', val2, ' Jump if false: ', val1, '== 0 -> jump to', val2)
                # index = val2 if val1 == 0 else index + 3

            elif opcode == 7:
                index = self.OpLessThan(val1, val2, dest, index)

                # self.program[dest] = 1 if val1 < val2 else 0
                # print(index, ':  ','Op:', opcode, '  ', mode1, ':', val1, '  ', mode2, ':', val2, ' Less than: ', val1, '=', val2, ' wrote ', self.program[dest], ' into ', dest)
                # index += 4

            elif opcode == 8:
                index = self.OpEquals(val1, val2, dest, index)
                # self.program[dest] = 1 if val1 == val2 else  0
                # print(index, ':  ','Op:', opcode, '  ', mode1, ':', val1, '  ', mode2, ':', val2, ' Equals: ', val1, '=', val2, ' wrote ', self.program[dest], ' into ', dest)
                # index += 4
            else:
                # print(index, ':  ','Op:', opcode, '  ', mode1, ':', val1)
                return self.outputList

            if mode3 == 1:
                print(index, ':  ','Op:', opcode, '  ', mode1, ':', val1, '  ', mode2, ':', val2, '  ', mode3, ':', dest)


        if len(self.outputList) > 0 :
            return self.outputList[-1] 
        else: 
            return self.program[index]

    def OpAdd(self, v1, v2, d, i):
        self.program[d] = v1 + v2
        return i + 4

    def OpMul(self, v1, v2, d, i):
        self.program[d] = v1 * v2
        return i + 4

    def OpLoad(self, v1, v2, d, i):
        self.program[v1] = self.GetNextInput()
        return i + 2

    def OpSave(self, v1, v2, d, i):
        self.AddToOutput(v1)
        return i + 2

    def OpJumpOnTrue(self, v1, v2, d, i):
        i = v2 if v1 != 0 else i + 3
        return i

    def OpJumpOnFalse(self, v1, v2, d, i):
        i = v2 if v1 == 0 else i + 3
        return i

    def OpLessThan(self, v1, v2, d, i):
        self.program[d] = 1 if v1 < v2 else 0
        return i + 4

    def OpEquals(self, v1, v2, d, i):
        self.program[d] = 1 if v1 == v2 else 0
        return i +4

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

