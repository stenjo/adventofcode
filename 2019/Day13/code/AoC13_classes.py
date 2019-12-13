# Advent of Code 2019: https://adventofcode.com/2019/day/13
# 
# 

import math
from matplotlib import pylab as pt, pyplot as plt

class ArcadeCabinet():

    width = None
    height = None
    comp = None
    panels = []
    tiles = {}
    pos = None
    direction = 0   # 0 = up. 1 = right, 2 = down, 3 = left

    def __init__(self, program):
        self.count = 0
        self.width = None
        self.comp = Compute(program)
        # self.comp.LoadInput([0])
        self.pos = (0,0)
        self.direction = 0

    def PaintAndMove(self, data):
        color, turn = data     #tuple (color,direction)
        panel = {'pos':self.pos, 'color':color}
        panelDict = self.ConvertToDict(self.panels)
        if self.pos not in panelDict:
            self.panels.append(panel)
        else:
            panelDict[self.pos] = {'pos':self.pos, 'color':color}
        
        if turn == 0: # Turn left
            self.direction -= 1
        else:
            self.direction += 1

        self.direction=self.direction % 4

        if self.direction == 0:  # up
            self.pos = (self.pos[0], self.pos[1]-1)
        elif self.direction == 1:  # right
            self.pos = (self.pos[0]+1, self.pos[1])
        elif self.direction == 2:  # down
            self.pos = (self.pos[0], self.pos[1]+1)
        elif self.direction == 3:  # left
            self.pos = (self.pos[0]-1, self.pos[1])
        else:
            print('Error in direction: ', self.direction)

        panelDict = self.ConvertToDict(self.panels)
        if self.pos not in panelDict:
            color = 0
        else:
            color = panelDict[self.pos]['color']
            
        return color

    def ConvertToDict(self, tup): 
        di = {}
        for a in tup: 
            di.setdefault(a['pos'], a)
        return di 

    def PaintPanels(self):
        color = 0
        self.comp.LoadInput([color])
        result = self.comp.RunFor2Outputs()
        while self.comp.ProgramFinished() == False:
            color = self.PaintAndMove(result)
            self.comp.LoadInput([color])
            result = self.comp.RunFor2Outputs()
    
    def WriteTiles(self):
        color = 0
        # self.comp.LoadInput([color])
        result = self.comp.RunFor3Outputs()
        while self.comp.ProgramFinished() == False:
            # color = self.PaintAndMove(result)
            # self.comp.LoadInput([color])
            result = self.comp.RunFor3Outputs()
            if len(result) == 3:
                x,y,tile = result
                pos = (x,y)
                panel = {'pos':pos, 'tile':tile}

                if tile == 2:
                    self.tiles[pos] = panel
                    print(result)

    def NumberOfPanelsPainted(self):
        return len(self.tiles)

    def PlotTiles(self):
        data = {
            'x': [d['pos'][0]    for d in self.tiles],
            'y': [d['pos'][1]    for d in self.tiles],
            'c': [d['tile']      for d in self.tiles],
        }
        plt.scatter('x','y', data=data)
        # plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'bo')
        # plt.axis([-1, self.width, self.height, -1])
        plt.show()

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

    def HasOutput(self):
        return len(self.outputList) > 0

    def Has2Outputs(self):
        return len(self.outputList) > 1

    def Has3Outputs(self):
        return len(self.outputList) > 2

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
    
    def RunFor2Outputs(self):
        self.outputList = []
        while self.Has2Outputs() == False and self.ProgramFinished() == False:
            self.RunOnce()

        print(self.outputList)
        color, direction = self.outputList

        return (color, direction)

    def RunFor3Outputs(self):
        self.outputList = []
        while self.Has3Outputs() == False and self.ProgramFinished() == False:
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
                dest = arg1 + self.relBase if modes % 10 == 2 else arg1
            
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

