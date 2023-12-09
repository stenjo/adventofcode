from Day09.NumberSequence import NumberSequence


def test_part1():
    assert len(NumberSequence(["1 2 3"]).sequences[0]) == 3
    assert NumberSequence(["1 2 3"]).sequences[0][2] == 3

    assert NumberSequence(["1 2 3"]).newSequence([1, 2, 3]) == [1, 1]

    assert NumberSequence(["1 2 3"]).allZeros([1, 2, 3]) == False
    assert NumberSequence(["1 2 3"]).allZeros([0, 2, 0]) == False
    assert NumberSequence(["1 2 3"]).allZeros([0, 0, 0]) == True

    assert NumberSequence(["1 2 3"]).nextNumber([1, 2, 3]) == 4
    assert NumberSequence(["0 3 6 9 12 15"]).nextNumber([0, 3, 6, 9, 12, 15]) == 18
    assert NumberSequence(["1 3 6 10 15 21"]).nextNumber([1, 3, 6, 10, 15, 21]) == 28
    assert (
        NumberSequence(["10 13 16 21 30 45"]).nextNumber([10, 13, 16, 21, 30, 45]) == 68
    )

    assert (
        NumberSequence(
            ["0 3 6 9 12 15", "1 3 6 10 15 21", "10 13 16 21 30 45"]
        ).sumOfNextNumbers()
        == 114
    )

    inputData = open("../data/input09.txt", "r").readlines()
    assert NumberSequence(inputData).sumOfNextNumbers() == 1995001648


def test_part2():
    assert (
        NumberSequence(
            ["0 3 6 9 12 15", "1 3 6 10 15 21", "10 13 16 21 30 45"]
        ).sumOfPreviousNumbers()
        == 2
    )
    inputData = open("../data/input09.txt", "r").readlines()
    assert NumberSequence(inputData).sumOfPreviousNumbers() == 988
