from Day05.SourceDestination import SourceDestination

def test_SourceDestination():
    
    assert SourceDestination("").items() == {}
    
    assert SourceDestination("50 98 2").items() == {98:50, 99:51}
    assert SourceDestination("50 98   2").items() == {98:50, 99:51}
    
    assert SourceDestination("0 69 1").items() == {69:0}
    
    sd = SourceDestination("50 98 2")
    sd.parseInput("0 69 1")
    assert sd.items() == {69:0, 98:50, 99:51}
    
    sd = SourceDestination()
    assert sd.items() == {}
    sd.parseInput("0 69 1")
    assert sd.items() == {69:0}
    assert sd.getMapped(69) == 0
    assert sd.getMapped(10) == 10
    
    