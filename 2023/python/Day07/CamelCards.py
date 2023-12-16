# Advent of Code 2023: https://adventofcode.com/2023/day/7

from Day07.Hand import Hand


class CamelCards:
    def __init__(self, handsList):
        self.hands = [Hand(hand) for hand in handsList if len(hand) > 6]
        
    def getSortedHands(self):
        hands = sorted( self.hands, key=lambda h: self.rank(h))
        return [(h.cards, h.bid) for h in hands]
        
    def getSortedHandsWithJoker(self):
        hands = sorted( self.hands, key=lambda h: self.rankWithJoker(h))
        return [(h.cards, h.bid) for h in hands]
        
    def totalWinnings(self):
        hands = sorted(self.hands, key=lambda h: self.rank(h))
        # hands = sorted(self.hands, key=functools.cmp_to_key(self.compare))
        score = 0
        for i, hand in enumerate(hands):
            score += hand.bid * (i + 1)

        return score
    
    def getRanking(self):
        hands = sorted(self.hands, key=self.rank)
        handsRank = {}
        for i, hand in enumerate(hands):
            handsRank[hand.cards] = (i + 1, hand.score())

        return handsRank

    def rank(self, hand):
        return hand.score(), hand.getCardRanking()

    def rankWithJoker(self, hand):
        return hand.scoreWithJoker(), hand.getCardRanking()

    def compare(self, a, b):
        if a.score() < b.score():
            return -1
        if a.score() > b.score():
            return 1
        if a.score() == b.score():
            if a.isStrongerThan(b):
                return 1
            else:
                return -1
        return 1
    
    def totalWinningsWithJoker(self):
        hands = sorted(self.hands, key=lambda hand: self.rankWithJoker(hand))
        score = 0
        for i, hand in enumerate(hands):
            score += hand.bid * (i + 1)

        return score

