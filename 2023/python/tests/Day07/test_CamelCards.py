from Day07.CamelCards import CamelCards
from Day07.Hand import Hand
from Day07.day_07_part_1 import playlist
from Day07.day_07_part_2 import playlist2

hands = [
"32T3K 765",
"T55J5 684",
"KK677 28 ",
"KTJJT 220",
"QQQJA 483"
]

hands2 = [
"32T3K 765",
"T55J5 684",
"KK677 28 ",
"KTJJT 220",
"QQQJA 483",
"22322 709",
"2346J 689"
]

def test_CamelCards():
    
    assert True == True
    
    assert len(CamelCards(hands).hands) == 5

def test_compare():
    assert CamelCards(hands).compare(Hand("QQQJA 483"), Hand("T55J5 684")) == 1
    assert CamelCards(hands).compare(Hand("T55J5 684"),Hand("QQQJA 483")) == -1
    assert CamelCards(hands).compare(Hand("QQQJA 483"), Hand("KK677 28")) == 1
    assert CamelCards(hands).compare(Hand("KK677 28"), Hand("QQQJA 483")) == -1
    assert CamelCards(hands).compare(Hand("53426 776"), Hand("2346J 689")) == 1


def test_getRanking():
    print(CamelCards(hands).getRanking())
    # assert CamelCards(hands).getRanking()["32T3K"] == (1,1)
    # assert CamelCards(hands).getRanking()["KTJJT"] == (2,2)
    # assert CamelCards(hands).getRanking()["KK677"] == (3,2)
    # assert CamelCards(hands).getRanking()["T55J5"] == (4,3)
    # assert CamelCards(hands).getRanking()["QQQJA"] == (5,3)
    # assert CamelCards(hands2).getRanking()["22322"] == (7,5)
    
    
def test_part1():
    assert CamelCards(hands).totalWinnings() == 6440
    inputData = open("../data/input07.txt", "r").readlines()
    
    assert CamelCards(inputData).getSortedHands() == playlist(inputData)
    assert CamelCards(inputData).totalWinnings() == 250474325

def test_part2():
    inputData = open("../data/input07.txt", "r").readlines()

    # assert CamelCards(inputData).getSortedHandsWithJoker() == playlist2(inputData)

    # assert CamelCards(inputData).totalWinningsWithJoker() ==  248909434
    