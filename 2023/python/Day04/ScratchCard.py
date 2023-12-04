
class ScratchCard:
    def __init__(self, cardStr):
        cardNoStr, numStr = (cardStr).strip().split(':')
        self.cardNo = int(cardNoStr.split(' ')[-1])
        myNumStr, winnersStr = numStr.split('|')
        self.numbers = [int(n) for n in myNumStr.split()]
        self.winners = [int(n) for n in winnersStr.split()]
        self.points = 0
        self.matching = 0
        self.getPoints()
        
    def getPoints(self):
        self.points = 0
        for n in self.numbers:
            if n in self.winners:
                if self.points == 0:
                    self.points = 1
                else:
                    self.points *= 2
                self.matching += 1
    