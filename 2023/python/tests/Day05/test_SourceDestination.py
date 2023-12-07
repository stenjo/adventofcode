from Day05.SourceDestination import SourceDestination


def test_SourceDestination():
    assert SourceDestination("").getMapped(88) == 88

    assert SourceDestination("50 98 2").getMapped(99) == 51

    assert SourceDestination("50 98   2").getMapped(98) == 50

    assert SourceDestination("0 69 1").getMapped(69) == 0

    sd = SourceDestination("50 98 2")
    sd.parseInput("0 69 1")
    assert sd.getMapped(69) == 0
    assert sd.getMapped(99) == 51
    assert sd.getSource(50) == 98
    assert sd.getSource(0) == 69
    assert sd.getSource(51) == 99
    assert sd.getSource(40) == 40
    assert sd.getDestRange() == [0,50,51]

    sd = SourceDestination()
    sd.parseInput("0 69 1")
    assert sd.getMapped(69) == 0
    assert sd.getMapped(10) == 10
