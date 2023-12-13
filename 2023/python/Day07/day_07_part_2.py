from collections import Counter

CARD_MAPPING = {'T': 'A', 'J': '.', 'Q': 'C', 'K': 'D', 'A': 'E'}


def get_type(hand):
    counts = Counter(hand)
    if len(counts) == 1:
        return 6
    if len(counts) == 2:
        if 4 in counts.values():
            return 5
        if 3 in counts.values() and 2 in counts.values():
            return 4
    if len(counts) == 3:
        if 3 in counts.values() and list(counts.values()).count(1) == 2:
            return 3
        if list(counts.values()).count(2) == 2:
            return 2
    if len(counts) == 4:
        return 1
    return 0


def find_all_combinations(hand):
    if not hand:
        return [""]

    current_card = hand[0]
    if current_card == 'J':
        possible_values = "23456789TQKA"
    else:
        possible_values = current_card

    combinations = [
        first_half + second_half
        for first_half in possible_values
        for second_half in find_all_combinations(hand[1:])
    ]

    return combinations


def find_max_type(hand):
    return max(map(get_type, find_all_combinations(hand)))


def get_order(hand):
    return [CARD_MAPPING.get(card, card) for card in hand]


def sorting(hand):
    return find_max_type(hand), get_order(hand)

def playlist2(data):
    plays = []
    for line in data:
        hand, bid = line.split()
        plays.append((hand, int(bid)))

    plays.sort(key=lambda play: sorting(play[0]))
    return plays

plays = []
with open("../data/input07.txt") as file:
    data = file.read().strip().split("\n")
    for line in data:
        hand, bid = line.split()
        plays.append((hand, int(bid)))

plays.sort(key=lambda play: sorting(play[0]))

ans = 0
for rank, (hand, bid) in enumerate(plays, 1):
    ans += bid * rank

print(ans)
