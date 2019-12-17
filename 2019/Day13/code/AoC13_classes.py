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
    tiles = []
    score = 0
    direction = 0   # 0 = up. 1 = right, 2 = down, 3 = left
    previousBall = None
    velocity = 0


    def __init__(self, program):
        self.count = 0
        self.width = None
        self.comp = Compute(program)
        self.comp.LoadInput([0])
        self.direction = 0

    def ConvertToDict(self, tup): 
        di = {}
        for a in tup: 
            di.setdefault(a['pos'], a)
        return di 

    
    def WriteTiles(self):
        color = 0
        self.tiles = []
        self.comp.progPtr=0
        # self.comp.LoadInput([color])
        result = self.comp.RunFor3Outputs()
        while self.comp.ProgramFinished() == False and self.comp.WaitingForInput() == False:
            # color = self.PaintAndMove(result)
            # self.comp.LoadInput([color])
            result = self.comp.RunFor3Outputs()
            if len(result) == 3:
                x,y,tile = result
                if x == -1:
                    self.score = tile
                    continue

                pos = (x,y)
                panel = {'pos':pos, 'tile':tile}
                tileDict = self.ConvertToDict(self.tiles)
                # if tile in [4,3]:
                #     self.PlotTiles()

                # if tile == 4:   # ball
                #     ball = self.GetBall()
                #     if ball != None:
                #         if self.previousBall != None:
                #             self.velocity = ball['pos'][0] - self.previousBall['pos'][0]
                #         self.previousBall = ball
                #         self.tiles.remove(ball)
                #     self.tiles.append(panel)
                #     print('  ball:', self.GetBall(), self.comp.outputList,'paddle:',self.GetPaddle(), self.comp.inputList)
                # elif tile == 3:     # paddle
                #     paddle = self.GetPaddle()
                #     ball = self.GetBall()
                #     if paddle != None:
                #         if ball != None:
                #             tilt = (ball['pos'][0] - x) - self.velocity*(y-ball['pos'][1])
                #             if tilt != 0:
                #                 tilt = int(tilt/abs(tilt))
                #             self.comp.LoadInput([tilt])
                #             print('tilt:', tilt, 'bx:',ball['pos'][0], 'px:',x, 'diff:',ball['pos'][0] - x, 'vel:', self.velocity )
                #         self.tiles.remove(paddle)
                #         panel['pos'] = (ball['pos'][0],21)
                #     self.tiles.append(panel)
                #     print('  ball:', self.GetBall(), self.comp.outputList,'paddle:',self.GetPaddle(), self.velocity, self.comp.inputList)

                # else:    
            # if pos not in tileDict and tile > 0:
                self.tiles.append(panel)
            # else:
            #     if tile == 0 and pos in tileDict:
            #         self.tiles.remove(tileDict[pos])
            #     else:
                # tileDict[pos] = {'pos':pos, 'tile':tile}
            

                    # print(panel)
        # if self.comp.WaitingForInput():
        #     self.comp.LoadInput([0])


    def RunGame(self):
        self.comp.LoadInput([2])
        self.comp.program[0] = 2    # Free running
        self.WriteTiles()
        self.comp.LoadInput([0])
        # while self.comp.ProgramFinished == False:
        while len(self.comp.inputList) > 0:
            self.WriteTiles()
            self.PlotTiles()
            self.comp.LoadInput([0])



    def GetBall(self):
        ballPos = [d for d in self.tiles if d['tile'] in [4]]
        if len(ballPos) == 0:
            return None
        else:
            return ballPos[0]

    def GetPaddle(self):
        paddlePos = [d for d in self.tiles if d['tile'] in [3]]
        if len(paddlePos) == 0:
            return None
        else:
            return paddlePos[0]

    def NumberOfBlocks(self):
        blockTiles = [d for d in self.tiles if d['tile'] in [2]]
        return len(blockTiles)

    def PlotTiles(self):
        data = {
            'x': [d['pos'][0]    for d in self.tiles],
            'y': [d['pos'][1]    for d in self.tiles],
            'c': [d['tile']*10      for d in self.tiles],
            'd': [d['tile']      for d in self.tiles]
        }
        plt.scatter('x','y',30, 'c', marker='s', data=data)
        # plt.plot([1, 2, 3, 4], [1, 4, 9, 16], 'bo')
        # plt.axis([-1, self.width, self.height, -1])
        plt.show()

class Compute():

    __program = []
    inputList = []
    outputList = []
    __progPtr = 0
    relBase = 0

    def __init__(self, data):
        self.LoadProgram(data)

    @property
    def program(self):
        return self.__program

    @program.setter
    def program(self, Value):
        self.__program = Value


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

