
from Day06.BoatRace import BoatRace

records = [
    "Time:      7  15   30",
    "Distance:  9  40  200"
]

def test_BoatRace():
    
    
    assert BoatRace(records).records[7] == 9
    assert BoatRace(records).records[15] == 40
    assert BoatRace(records).records[30] == 200
    
    assert BoatRace(records).calculateRange(0,0) == 0
    assert BoatRace(records).calculateRange(1,7) == 6
    assert BoatRace(records).calculateRange(2,7) == 10
    assert BoatRace(records).calculateRange(3,7) == 12
    assert BoatRace(records).calculateRange(4,7) == 12
    assert BoatRace(records).calculateRange(5,7) == 10
    assert BoatRace(records).calculateRange(6,7) == 6
    assert BoatRace(records).calculateRange(7,7) == 0
    
    assert BoatRace(records).getWinningWays(7,9) == 4
    assert BoatRace(records).getWinnerPresses() == [4,8,9]
    
    inputData = open("../data/input06.txt", "r").readlines()
    assert BoatRace(inputData).getTotal() == 1084752
    
    assert BoatRace(records).oneRace == (71530, 940200)
    assert BoatRace(inputData).getTotalOneRace() == 28228952
    