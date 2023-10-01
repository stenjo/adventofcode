from Day03.spiral import steps_carried

def test_steps_carried():
    
    assert steps_carried(1) == 0
    assert steps_carried(12) == 3
    # assert steps_carried(23) == 2
    # assert steps_carried(1024) == 31
    
    # assert steps_carried(368078) == 371
    