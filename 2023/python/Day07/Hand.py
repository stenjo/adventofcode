
class Hand:
    def __init__(self, handStr):
        self.cards = handStr.strip().split(' ')[0]
        self.bid = int(handStr.strip().split(' ')[1])
        self.rank = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
    
    def isFiveOfaKind(self):
        return len(list(set(list(self.cards)))) == 1
    
    def isFourOfaKind(self):
        cards = list(self.cards)
        cards.sort()
        return len(list(set(cards[:5]))) == 1 or len(list(set(cards[1:]))) == 1
    
    def isFullHouse(self):
        cards = list(self.cards)
        cards.sort()
        return (len(list(set(cards[:3]))) == 1 and len(list(set(cards[3:]))) == 1) or (len(list(set(cards[:2]))) == 1 and len(list(set(cards[2:]))) == 1)
            
    def isThreeOfaKind(self):
        cards = list(self.cards)
        cards.sort()
        for c in set(cards):
            if self.cards.count(c) == 3:
                return True      
            
        return False  
            
    def isTwoPairs(self):
        return self.getPairs() == 2

    def isOnePair(self):
        return self.getPairs() == 1
    
    def score(self):
        
        if self.isFiveOfaKind():    return 1000000
        if self.isFourOfaKind():    return 100000
        if self.isFullHouse():      return 10000
        if self.isThreeOfaKind():   return 1000
        if self.isTwoPairs():       return 100
        if self.isOnePair():        return 20
        
        return self.highestCard()
    
    def highestCard(self):
        cards = sorted(list(self.cards))
        return max([(len(self.rank) - self.rank.index(c)) for c in cards])
        
    def isStrongerThan(self, hand):
        for i, c in enumerate(self.cards):
            if self.cardIsGreater(c, hand.cards[i]) > 0: return True
            if self.cardIsGreater(c, hand.cards[i]) < 0: return False
            
        return False       
        
    def cardIsGreater(self, card1, card2):
        if card1 not in self.rank: 
            raise Exception("Not a valid card; ", card1)
        if card2 not in self.rank: 
            raise Exception("Not a valid card; ", card2)
        return self.rank.index(card2) - self.rank.index(card1)
    
    def getPairs(self):
        cards = sorted(list(self.cards))
        pairs = 0
        for c in set(cards):
            if self.cards.count(c) == 2:
                pairs += 1
        return pairs
        
