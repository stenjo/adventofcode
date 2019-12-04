# Advent of Code 2019: https://adventofcode.com/2019/day/4
# 
# 
import math

class FindPassword():

    rangeLow = 111111
    rangeHigh = 999999

    def __init__(self, rangeLimits = '111111-999999'):
        super().__init__()
        self.rangeLow, self.rangeHigh = map(lambda x: int(x), rangeLimits.split('-'))
        
    def IntToArray(self, num):
        return [int(i) for i in str(num)]

    def ArrayToInt(self, numArray):
        return int("".join(map(str, numArray)))

    def Length(self, num):
        if num > 99999 and num < 1000000:
            return True
        else:
            return False

    def IsWithinRange(self, num):
        if num >= self.rangeLow and num <= self.rangeHigh:
            return True
        else:
            return False

    def HasAdjacent(self, num):
        d = 99
        for n in self.IntToArray(num):
            if n == d:
                return True
            else:
                d = n
        return False

    def HasAdjacentNL(self, num):
        d = 99
        p = 98
        double = False
        for n in self.IntToArray(num):
            if n == d and p != n:
                double = True
            else:
                double = False
            p = d
            d = n

        return double

    def Increasing(self, num):
        d = 0
        for n in self.IntToArray(num):
            if n >= d:
                d = n
            else:
                return False

        return True
        
    def IsValid(self, num):
        if self.Length(num) \
            and self.IsWithinRange(num) \
            and self.HasAdjacent(num) \
            and self.Increasing(num):
            return True
        return False

    def SetDigits(self, digitList, fromIndex, value):
        for i in range(fromIndex, len(digitList)):
            digitList[i] = value

    def Passwords(self):
        passWords = []
        for passwd in range(self.rangeLow, self.rangeHigh+1):

            if self.IsValid(passwd) == True:
                passWords.append(passwd)

        return len(passWords)

    def IsValidNL(self, num):
        if self.Length(num) \
            and self.IsWithinRange(num) \
            and self.HasAdjacentNL(num) \
            and self.Increasing(num):
            return True
        return False

    def PasswordsNL(self):
        passWords = []
        for passwd in range(self.rangeLow, self.rangeHigh+1):

            if self.IsValidNL(passwd) == True:
                passWords.append(passwd)

        return len(passWords)


