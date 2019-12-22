
import parser

class SpaceDeck():

    deck = []

    def __init__(self, length):
        super().__init__()
        self.deck = list(range(length))

    def CutN(self, n):
        print('cut', n)
        self.deck = self.deck[n:] + self.deck[:n]
        return self.deck

    def DealIntoNew(self):
        print('Deal into new stack')
        self.deck.reverse()
        return self.deck

    def DealWithIncrement(self, n):

        print('Deal with increment', n)
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
            return self.DealWithIncrement(num)
        elif instruction.find('deal into new stack') > -1:
            # return 'DealIntoNew'
            if num != None:
                print("Error on number extraction at instruction:", instruction, " got:",numbers)
                exit(1)
            return self.DealIntoNew()
        elif instruction.find('cut') > -1:
            # return 'CutN'
            if num == None:
                print("Error on number extraction at instruction:", instruction, " got:",numbers)
                exit(1)
            return self.CutN(num)
        else:
            print("Error on instrunction parsing at instruction:", instruction)
            exit(1)


        return ''

    def RunDeal(self, instructions):
        print(len(instructions), "instrunctions detected")
        for i in instructions:
            deck = self.ParseInstructions(i)

        return deck
    
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

