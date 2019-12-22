# Advent of Code 2019: https://adventofcode.com/2019/day/21
# 
# 

import inspect
from functools import reduce

class SpringDroid():

    comp = None
    def __init__(self):
        super().__init__()
        infile = open('data/input_21.txt','r')
        program = infile.readline().strip().split(',')
        self.comp = Compute(program)

    def LoadAsciiProgram(self, prog):
        code = []
        for l in prog:
            code += [ord(a) for a in l]
            code.append(10)
            self.comp.LoadInput(code)

    def RunProgram(self):
        return self.comp.RunForNewline()
        

class SpaceMap():

    comp = None
    spaceMap = {}
    program = None

    def __init__(self, program):
        self.count = 0
        self.width = 0
        self.program = program
        self.comp = Compute(program)
        # self.comp.LoadInput([0])
        self.direction = 0

    def ConvertToDict(self, tup): 
        di = {}
        for a in tup: 
            di.setdefault(a['pos'], a)
        return di 

    def LoadMap(self, m):
        y = 0
        for r in m:
            x = 0
            for p in r:
                self.spaceMap[(x,y)] = p
                x += 1
            y += 1

        return (x,y)

    def GetAffectedCells(self, chars = '#O'):
        l = filter(lambda x: x in chars, list(self.spaceMap.values()))
        return len(list(l))

    def WriteTractorMap(self):
        for y in range(100):
            self.WriteMapLine(0,y)

        return len(self.spaceMap)

    def WriteMapLine(self, xStart = 0, yLine = 0):
        for x in range(xStart, yLine+1):
            self.comp.LoadInput([x,yLine])
            self.comp.LoadProgram(self.program)
            traction = self.comp.RunCompute()
            if traction == 1:
                self.spaceMap[(x,yLine)] = '#'


    def WriteBeamMap(self, size):
        l = [self.spaceMap[(x,size-1)] for x in range(size)]
        return len(self.spaceMap)

    def PrintSpaceMap(self):
        maxX,maxY = max(list(self.spaceMap))
        lines = 0
        print()
        for y in range(maxY+1):
            line = []
            for x in range(maxX+1):
                if (x,y) in self.spaceMap:
                    line.append(self.spaceMap[(x,y)])
                else:
                    line.append(' ')

            print(''.join(line))
            lines += 1

        return(lines)

    def SquareWithinBeam(self, x, y, size):
        # fits horizontally
        positions = [(n,y) for n in range(x,x+size)]
        fitsX = reduce((lambda acc, n: acc and self.spaceMap[n] in '#O'), positions)

        # fits vertically
        positions = [(x,n) for n in range(y,y+size)]
        fitsY = reduce((lambda acc, n: acc and self.spaceMap[n] in '#O'), positions)

        return fitsX and fitsY

    def BeamPosInRow(self, y):
        q = {k: v for k, v in self.spaceMap.items() if v in '#O' and k[1] == y}
        return q

    def FindSquareDistance(self, size = 100):

        self.WriteTractorMap()
        maxX,maxY = max(list(self.spaceMap)) 

        beam = self.BeamPosInRow(maxY)

        x1,y1 = min(beam)
        k1 = x1/y1

        l1 = y1/len(beam)
        y = l1 * size
        x = k1 * y
        dx = k1 * size



        # firstLine = int(candY[0]/len(beam)*size)



        y = 309                
        self.WriteMapLine(y)          
        while len(self.BeamPosInRow(y)) < size:
            y += 1
            maxX,maxY = max(list(self.spaceMap)) 
            if y >= maxY:
                self.WriteMapLine(y)          
            print(y)
        found = False
        while found == False:
            points = self.BeamPosInRow(y)
            for p in points:
                x,n = p
                if self.SquareWithinBeam(x,y, size):
                    found = True
                    return x*10000+y
            print(y, len(points))
            y += 1
            maxX,maxY = max(list(self.spaceMap)) 
            if y >= maxY:
                self.WriteMapLine(y)          

        return x*10000+y


class Compute():

    program = []
    inputList = []
    outputList = []
    progPtr = 0
    relBase = 0

    def __init__(self, data):
        self.LoadProgram(data)

    def LoadInput(self, data):
        self.inputList = []
        for n in data:
            self.inputList.append(n)
        self.inputList.reverse()

    def LoadProgram(self, data):
        self.program = list(map(int, data))
        self.progPtr = 0
        self.relBase = 0
    
    def AddToOutput(self, data):
        self.outputList.append(data)

    def GetNextInput(self):
        return self.inputList.pop() if len(self.inputList) > 0 else None

    def ProgramFinished(self):
        return self.program[self.progPtr] == 99

    def WaitingForInput(self):
        return True if self.program[self.progPtr] == 3 and len(self.inputList) == 0 else False

    def HasOutput(self):
        return len(self.outputList) > 0

    def Has2Outputs(self):
        return len(self.outputList) > 1

    def Has3Outputs(self):
        return len(self.outputList) > 2

    def HasNLInOutputs(self):
        return 10 in self.outputList

    def RunCompute(self):
        self.progPtr = 0
        self.outputList = []
        while self.ProgramFinished() == False:
            self.RunOnce()

        return self.outputList[-1] if len(self.outputList) > 0 else self.program[self.progPtr]

    def RunForOutput(self):
        # self.progPtr = 0
        self.outputList = []
        while self.HasOutput() == False and self.ProgramFinished() == False:
            self.RunOnce()

        return self.outputList

    def RunForNewline(self):
        self.outputList = []
        while self.HasNLInOutputs() == False and self.ProgramFinished() == False:
            self.RunOnce()

        # print(self.outputList)
        return ''.join([chr(a) for a in self.outputList])
        
    
    def RunFor2Outputs(self):
        self.outputList = []
        while self.Has2Outputs() == False and self.ProgramFinished() == False:
            self.RunOnce()

        print(self.outputList)
        color, direction = self.outputList

        return (color, direction)

    def RunFor3Outputs(self):
        self.outputList = []
        while self.Has3Outputs() == False and self.ProgramFinished() == False and self.WaitingForInput() == False:
            self.RunOnce()

        # print(self.outputList)
        if len(self.outputList) == 3:
            x, y, t = self.outputList
            return (x,y,t)
        else:
            return self.outputList

    def GetValue(self, arg, mode):
        val = None
        if mode == 0:           # Position mode
            val = self.GetValueAt(arg)
        elif mode == 1:         # Immediate mode
            val = arg
        elif mode == 2:         # Relative mode
            val = self.GetValueAt(self.relBase + arg)

        return val

    def RunOnce(self):
            self.ExtendMemory(self.progPtr + 3)     # Make sure the program is long enough

            modes = self.program[self.progPtr] // 100
            opcode = self.program[self.progPtr] % 100
            
            arg1 = self.program[self.progPtr+1]
            val1 = self.GetValue(arg1, modes % 10) 

            arg2 = self.program[self.progPtr+2]
            val2 = self.GetValue(arg2, modes // 10 % 10)

            arg3 = self.program[self.progPtr+3]
            dest = self.GetValue(arg3, 1)

            dest = arg3 + self.relBase if modes // 100 % 10 == 2 else arg3
            if (opcode in [3,4]):
                if opcode == 3:     # Waiting for input
                    if len(self.inputList) == 0:
                        return

                dest = arg1 + self.relBase if modes % 10 == 2 else arg1
            
            # print(self.progPtr, ':', opcode, arg1, arg2, '(', val1, val2, ')')
            # print(self.program[380:390])
            dispatch = {
                1: self.OpAdd,
                2: self.OpMul,
                3: self.OpLoad,
                4: self.OpSave,
                5: self.OpJumpOnTrue,
                6: self.OpJumpOnFalse,
                7: self.OpLessThan,
                8: self.OpEquals,       # Jump to arg3 if arg1 = arg2
                9: self.OpAdjRBase
            }

            self.progPtr = dispatch[opcode](val1, val2, dest, self.progPtr)


    def OpAdd(self, v1, v2, d, i):
        self.ExtendMemory(d)
        self.program[d] = v1 + v2
        return i + 4

    def OpMul(self, v1, v2, d, i):
        self.ExtendMemory(d)
        self.program[d] = v1 * v2
        return i + 4

    def OpLoad(self, v1, v2, d, i):
        self.ExtendMemory(d)
        self.program[d] = self.GetNextInput()
        if self.program[d] == None:
            print(i, ':', 3, v1, v2, '(', d, ')')
            print(self.outputList)
            exit(1)

        return i + 2

    def OpSave(self, v1, v2, d, i):
        self.AddToOutput(v1)
        return i + 2

    def OpJumpOnTrue(self, v1, v2, d, i):
        i = v2 if v1 != 0 else i + 3
        self.ExtendMemory(i)
        return i

    def OpJumpOnFalse(self, v1, v2, d, i):
        i = v2 if v1 == 0 else i + 3
        self.ExtendMemory(i)
        return i

    def OpLessThan(self, v1, v2, d, i):
        self.ExtendMemory(d)
        self.program[d] = 1 if v1 < v2 else 0
        return i + 4

    def OpEquals(self, v1, v2, d, i):
        self.ExtendMemory(d)
        self.program[d] = 1 if v1 == v2 else 0
        return i + 4

    def OpAdjRBase(self, v1, v2, d, i):
        self.relBase += v1
        return i + 2

    def GetValueAt(self, progPtr):
        self.ExtendMemory(progPtr)
        return self.program[progPtr]

    def GetOutputs(self):
        return self.outputList

    def ExtendMemory(self, ptrNeed):
        if (ptrNeed + 1) > len(self.program):
            missing = ptrNeed + 1 - len(self.program)
            self.program += [0 for i in range(missing)]

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
