# Advent of Code 2019: https://adventofcode.com/2019/day/7
# 
# 
import math

class AmplificationCircuit():

    program = []
    phaseList = []
    inData = None

    def __init__(self, input, program):
        super().__init__()
        self.inData = input
        self.program = program

    def RunPhaseSet(self, phases):
        ampList = [Amplifier(self.program) for i in range(5)]
        o = 0
        for i in range(5):
            o = ampList[i].Amplify(phases[i], o)
        return o

    def RunLoopbackPhaseSet(self, phases):
        ampList = [Amplifier(self.program) for i in range(5)]
        o = [0]
        # phases.reverse()
        for i in range(5):  # first round
            o = ampList[i].AmplifyLoopback([phases[i]] + o)
            # print("Amp:", i, phases, phases[i], o)

        done = False
        while done == False:
            saved = o
            for i in range(5):  # first round
                res = ampList[i].AmplifyLoopback(o)
                # print("Amp:", i, phases, res, saved)

                if len(res):
                    o = res
                else:
                    done = True

        return saved

    def GetNextPhaseSetting(self, phaseArray):
        if len(phaseArray) > 0:
            return phaseArray.pop()
        else:
            return None

    def GetMaxAmplification(self):
        signal = 0
        phaseSet = self.GetPhaseSets()

        for s in phaseSet:
            result = self.RunPhaseSet(s)
            if signal < result:
                signal = result

        return signal

    def GetPhaseSets(self, allowedSet = [0,1,2,3,4]):
        notAllowed = set(range(10))-set(allowedSet)
        allowedSet.sort()
        rangeStart = int("".join([str(i) for i in allowedSet]))
        allowedSet.reverse()
        rangeEnd = int("".join([str(i) for i in allowedSet]))+1
        phaseSet = []
        for i in range(rangeStart,rangeEnd):
            digits = [int(d) for d in str(i).rjust(5,'0')]
            if len(set(digits)) == 5:   # Check that there are 5 unique digits in the number
                if len(set(digits) - notAllowed) == 5:
                    phaseSet.append(digits)

        return phaseSet

    def GetMaxLoopbackAmp(self):
        signal = 0
        phaseSet = self.GetPhaseSets([5,6,7,8,9])

        for s in phaseSet:
            result = self.RunLoopbackPhaseSet(s)
            if signal < result[0]:
                signal = result[0]

        return signal
                

    
class Amplifier():

    computer = None

    def __init__(self, program):
        super().__init__()
        self.computer = Compute(program)
    
    def Amplify(self, phase, indata):
        if phase is not None:
            self.computer.LoadInput([phase, indata])
        else:
            self.computer.LoadInput([indata])

        return self.computer.RunCompute()

    def AmplifyLoopback(self, indata):
        self.computer.LoadInput(indata)
        return self.computer.RunForOutput()

class Compute():

    program = []
    inputList = []
    outputList = []
    progPtr = 0

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
    
    def AddToOutput(self, data):
        self.outputList.append(data)

    def GetNextInput(self):
        return self.inputList.pop() if len(self.inputList) > 0 else None

    def ProgramFinished(self):
        return self.program[self.progPtr] == 99

    def HasOutput(self):
        return len(self.outputList) > 0

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


    def RunOnce(self):
            modes = self.program[self.progPtr] // 100

            opcode = self.program[self.progPtr] % 100

            arg1 = self.program[self.progPtr+1]
            val1 = arg1 if modes % 10 == 1 or opcode == 3 else self.program[arg1]

            arg2 = self.program[self.progPtr+2] if self.progPtr+2 < len(self.program) else None
            val2 = self.program[arg2] if modes // 10 % 10 == 0 and arg2 < len(self.program) else arg2

            dest = self.program[self.progPtr+3] if self.progPtr + 3 < len(self.program) else None

            dispatch = {
                1: self.OpAdd,
                2: self.OpMul,
                3: self.OpLoad,
                4: self.OpSave,
                5: self.OpJumpOnTrue,
                6: self.OpJumpOnFalse,
                7: self.OpLessThan,
                8: self.OpEquals
            }

            self.progPtr = dispatch[opcode](val1, val2, dest, self.progPtr)


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

    def GetValueAt(self, progPtr):
        return self.program[progPtr]

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



