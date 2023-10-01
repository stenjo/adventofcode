from Day03.spiral import steps_carried, steps_adjacent

def test_steps_carried():
    
    assert steps_carried(1) == 0
    assert steps_carried(12) == 3
    assert steps_carried(23) == 2
    assert steps_carried(1024) == 31
    
    assert steps_carried(368078) == 371
    
def test_steps_adjacent():
    
    assert steps_adjacent(1) == 2
    assert steps_adjacent(368078) == 369601
    