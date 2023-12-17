from Day16.Entrapment import Entrapment

testData = open("../data/testData16.txt", "r").readlines()


def test_Entrapment():
    assert Entrapment([]) != None
    assert len(Entrapment(testData).tiles[6]) == 10

    assert Entrapment(testData).countEnergized() == 46

    inputData = open("../data/input16.txt", "r").readlines()
    assert Entrapment(inputData).countEnergized() == 6978

    assert Entrapment(testData).countEnergized(("V", (3, 0))) == 51

    assert Entrapment(testData).getMaxStarters() == 51
    assert Entrapment(inputData).getMaxStarters() == 7315
