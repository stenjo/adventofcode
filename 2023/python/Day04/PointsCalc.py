from Day04.ScratchCard import ScratchCard

class PointsCalc:
    def __init__(self, cards):
        self.cards = [ScratchCard(c) for c in cards]
        self.points = self.getSumOfPoints()
        self.count = self.getCopiesCount()
        
    def getSumOfPoints(self):
        sum = 0
        for c in self.cards:
            sum += c.points
            
        return sum
    
    def getCopiesCount(self):
        cards = [1 for _ in self.cards]
        
        print(cards)
        for i, c in enumerate(self.cards):
            for j in range(self.cards[i].matching):
                cards[i+1+j] += cards[i]
        return sum(cards)
    
            
        
