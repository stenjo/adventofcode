
from Day07.Hand import Hand

hands = [
"32T3K 765",
"T55J5 684",
"KK677 28",
"KTJJT 220",
"QQQJA 483"
]

def test_Hand():
    assert Hand("32T3K 765").bid == 765
    
def test_isFiveOfaKind():
    assert Hand("32T3K 765").isFiveOfaKind() == False
    assert Hand("AAAAA 765").isFiveOfaKind() == True
    assert Hand("AAAJJ 765").isFiveOfaKindWithJoker() == True
    assert Hand("AAAJJ 765").isFiveOfaKind() == False
    assert Hand("J55J5 684").isFiveOfaKindWithJoker() == True
    assert Hand("J55J5 684").isFiveOfaKind() == False
    
def test_isFourOfaKind():
    assert Hand("AAAAA 765").isFourOfaKind() == True
    assert Hand("33332 765").isFourOfaKind() == True
    assert Hand("77788 765").isFourOfaKind() == False
    assert Hand("2AAAA 765").isFourOfaKind() == True
    assert Hand("AA3AA 765").isFourOfaKind() == True
    assert Hand("22322 709").isFourOfaKind() == True
    assert Hand("QQQJA 483").isFourOfaKindWithJoker() == True
    assert Hand("QQQJA 483").isFourOfaKind() == False
    
def test_isFullHouse():
    assert Hand("AA3AA 765").isFullHouse() == False
    assert Hand("AA333 765").isFullHouse() == True
    assert Hand("A3A3A 765").isFullHouse() == True
    assert Hand("77788 765").isFullHouse() == True
    assert Hand("77888 765").isFullHouse() == True
    assert Hand("T55J5 684").isFullHouse() == False
    assert Hand("QQQJA 483").isFullHouse() == False
    
def test_isThreeOfaKind():
    assert Hand("AA3AA 765").isThreeOfaKind() == False
    assert Hand("AA333 765").isThreeOfaKind() == True
    assert Hand("77A88 765").isThreeOfaKind() == False
    assert Hand("77888 765").isThreeOfaKind() == True
    assert Hand("KTJJT 220").isThreeOfaKind() == False
    assert Hand("T55J5 684").isThreeOfaKind() == True
    assert Hand("QQQJA 483").isThreeOfaKind() == True
    
def test_isTwoPairs():
    assert Hand("AA3AA 765").isTwoPairs() == False
    assert Hand("AA333 765").isTwoPairs() == False
    assert Hand("77788 765").isTwoPairs() == False
    assert Hand("77888 765").isTwoPairs() == False
    assert Hand("KTJJT 220").isTwoPairs() == True

def test_isOnePair():
    assert Hand("KTJJT 220").isOnePair() == False
    assert Hand("32T3K 765").isOnePair() == True

def test_isStrongerThan():
    assert Hand("33332 10").isStrongerThan(Hand("2AAAA 12")) == True
    assert Hand("77788 10").isStrongerThan(Hand("77888 12")) == False
    assert Hand("KK677 28").isStrongerThan(Hand("7KTJJT 220")) == True
    assert Hand("7KTJJT 220").isStrongerThan(Hand("KK677 28")) == False
    assert Hand("2346J 689").isStrongerThan(Hand("53426 776")) == False
    
def test_cardIsGreater():
    assert Hand("KK677 28").cardIsGreater('7', 'K') < 0
    assert Hand("KK677 28").cardIsGreater('K', 'K') == 0
    assert Hand("KK677 28").cardIsGreater('K', 'K') == 0

def test_score():
    assert Hand("23456 77").score() == 0
    assert Hand("AAAAA 765").score() == 1000000
    assert Hand("22322 709").score() == 100000
    assert Hand("2345A 77").score() == 0    
    assert Hand("T55J5 684").score() == 1000
    assert Hand("QQQJA 483").score() == 1000
    assert Hand("KTJJT 220").score() == 100
    assert Hand("53426 776").score() == 0
    assert Hand("2346J 689").score() == 0

def test_getCardRanking():
    assert Hand("2346J 987").getCardRankingWithJoker() == [2,3,4,6,1]    
    
def test_scoreWithJoker():
    assert Hand("2346J 987").scoreWithJoker() == 20    
    assert Hand("79J27 987").scoreWithJoker() == 1000    
    assert Hand("8933J 987").scoreWithJoker() == 1000    
    assert Hand("553JQ 987").scoreWithJoker() == 1000    
    assert Hand("8J8QQ 987").scoreWithJoker() == 10000    
    assert Hand("J4999 987").scoreWithJoker() == 100000    
    assert Hand("4TJT6 987").scoreWithJoker() == 1000    
    assert Hand("KJ46J 987").scoreWithJoker() == 1000    
    assert Hand("8KJJJ 987").scoreWithJoker() == 100000    
    assert Hand("6J778 987").scoreWithJoker() == 1000    
    assert Hand("4JJ2K 987").scoreWithJoker() == 1000    
    assert Hand("57ATJ 987").scoreWithJoker() == 20    
    assert Hand("QQQJ6 987").scoreWithJoker() == 100000    
    assert Hand("JK646 987").scoreWithJoker() == 1000    
    assert Hand("94J64 987").scoreWithJoker() == 1000
    assert Hand("JKJJJ 987").scoreWithJoker() == 1000000 
    assert Hand("2346J 987").scoreWithJoker() == 20   
        