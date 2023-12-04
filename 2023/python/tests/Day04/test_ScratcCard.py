from Day04.ScratchCard import ScratchCard

testCards = [
"Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
"Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
"Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
"Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
"Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
"Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
]

def test_load_cards():
    s = ScratchCard("Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53")
    assert(s.cardNo) == 1
    assert(len(s.numbers)) == 5
    assert(s.numbers[0]) == 41
    assert(len(s.winners)) == 8
    assert(s.winners[0]) == 83
    assert(s.points) == 8
    assert(s.matching) == 4
    
    assert(ScratchCard(testCards[0]).points) == 8
    assert(ScratchCard(testCards[1]).points) == 2
    assert(ScratchCard(testCards[2]).points) == 2
    assert(ScratchCard(testCards[3]).points) == 1
    assert(ScratchCard(testCards[4]).points) == 0
    assert(ScratchCard(testCards[5]).points) == 0

