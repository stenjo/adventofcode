from Day07.CamelCards import CamelCards
from Day07.Hand import Hand

hands = [
"32T3K 765",
"T55J5 684",
"KK677 28 ",
"KTJJT 220",
"QQQJA 483"
]

def test_CamelCards():
    
    assert True == True
    
    assert len(CamelCards(hands).hands) == 5

def test_compare():
    assert CamelCards(hands).compare(Hand("QQQJA 483"), Hand("T55J5 684")) == 1
    assert CamelCards(hands).compare(Hand("T55J5 684"),Hand("QQQJA 483")) == -1
    assert CamelCards(hands).compare(Hand("QQQJA 483"), Hand("KK677 28")) == 1
    assert CamelCards(hands).compare(Hand("KK677 28"), Hand("QQQJA 483")) == -1


def test_getRanking():
    print(CamelCards(hands).getRanking())
    assert CamelCards(hands).getRanking()["32T3K"] == (1,20)
    assert CamelCards(hands).getRanking()["KTJJT"] == (2,100)
    assert CamelCards(hands).getRanking()["KK677"] == (3,100)
    assert CamelCards(hands).getRanking()["T55J5"] == (4,1000)
    assert CamelCards(hands).getRanking()["QQQJA"] == (5,1000)
    
    
def test_part1():
    assert CamelCards(hands).totalWinnings() == 6440
    inputData = open("../data/input07.txt", "r").readlines()
    # assert CamelCards(inputData).totalWinnings() == 250474325

def test_part2():
    248909434
    