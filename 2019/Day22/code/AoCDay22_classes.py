# Advent of Code classes Advent of Code 2019, Day 22
#
# todo: Implement solution to part 2 using https://codeforces.com/blog/entry/72593
#

import parser

class SpaceDeck():

    deck = []
    coefficients = []

    def __init__(self, length):
        super().__init__()
        self.deckSize = length

    def CutN(self, n):
        # print('cut', n)
        temp = self.deck[n:] + self.deck[:n]
        self.deck = list(temp)
        return self.deck

    def DealIntoNew(self):
        # print('Deal into new stack')
        self.deck.reverse()
        return self.deck

    def DealWithIncrement(self, n):
        # print('Deal with increment', n)
        i = 0
        l = len(self.deck)
        temp = [None for n in range(l)]
        for x in self.deck:
            if temp[i%l] != None:
                print("Error on dealing with increment. overwrite position:", i%l, i)
                exit(1)
            temp[i%l] = x
            i += n
        
        if None in temp:
            print("Error on dealing with increment. Unused position:", temp.index(None))
            exit(1)

        self.deck = list(temp)
        return self.deck
    
    def is_digit(self,n):
        try:
            int(n)
            return True
        except ValueError:
            return  False

    def ParseInstructions(self, instruction):
        # self.coefficients = []
        numbers = [int(n) for n in instruction.split() if self.is_digit(n)]
        if len(numbers) > 1:
            print("Error on number extraction at instruction:", instruction, " got:",numbers)
            exit(1)

        num = None
        if len(numbers) == 1:
            num = numbers.pop()

        if instruction.find('deal with increment') > -1:
            # return 'DealWithIncrement'
            if num == None:
                print("Error on number extraction at instruction:", instruction, " got:",numbers)
                exit(1)
            self.coefficients.append((num,0))   # "deal with increment n^n ": f(x)=n⋅x  mod m f(x)=n⋅x  mod m, so a=n,b=0
            return self.DealWithIncrement(num)
        elif instruction.find('deal into new stack') > -1:
            # return 'DealIntoNew'
            if num != None:
                print("Error on number extraction at instruction:", instruction, " got:",numbers)
                exit(1)
            self.coefficients.append((-1,-1))     # "deal into new stack": f(x)=−x−1  mod m, so a=−1,b=−1
            return self.DealIntoNew()
        elif instruction.find('cut') > -1:
            # return 'CutN'
            if num == None:
                print("Error on number extraction at instruction:", instruction, " got:",numbers)
                exit(1)
            self.coefficients.append((1,-num))     # "cut n^n": f(x)=x−n  mod m, so a=1,b=−n
            return self.CutN(num)
        else:
            print("Error on instrunction parsing at instruction:", instruction)
            exit(1)

        return ''

    def GetShuffleCoeffs(self):
        m = self.deckSize
        coeffs= self.coefficients.pop(0)    # removes the first one so the for-loop takes the rest
        for s in self.coefficients:
            a,b = coeffs
            c,d = s
            coeffs = (a*c % m, (b*c+d) % m)

        return coeffs

    def RunDeal(self, instructions):
        self.deck = list(range(self.deckSize))
        for i in instructions:
            deck = self.ParseInstructions(i)

        return deck

    def RunFDeal(self, instructions, x):
        
        for i in instructions:
            deck = self.ParseInstructions(i)

        m = self.deckSize
        a,b = self.GetShuffleCoeffs()
        
        return int(a*x + b) % m

    def GetCardAtPosOnDeck(self, instructions, x, k):

        for i in instructions:
            deck = self.ParseInstructions(i)

        m = self.deckSize
        a,b = self.GetShuffleCoeffs()
        print(a,b)
        A = pow(a,k)
        B = (b * (1-pow(a,k)))*pow(1-a, -1)
        print(A,B)

        card = ((x-B)/A) % m
        return int(card)

    def RunDealUntilSorted(self, instructions):
        x = 0
        done = False
        l = [n for n in self.deck if self.deck.index(n) != n]
        while done == False:
            x += 1
            for i in instructions:
                deck = self.ParseInstructions(i)
            l = [n for n in self.deck if self.deck.index(n) != n]
            if len(l) == 0:
                done = True

        return x

    
    def comparefiles(self, file1, file2):
        infile1 = open('data/'+file1,'r')
        infile2 = open('data/'+file2,'r')
        lines1 = infile1.readlines()
        lines2 = infile2.readlines()
        for i in range(len(lines1)):
            if lines1[i].lower() != lines2[i].lower():
                print("Files differ:", lines1[i])
                exit(1)

        print('Files match!')

