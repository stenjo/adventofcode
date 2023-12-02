from Day02.CubeGame import CubeGame, possibleSum, powerSum

games = [        
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
]

limits = {"red": 12, "green": 13, "blue": 14}

def test_game_isPossible():
    game = CubeGame(games[0])
    assert game.cubes["blue"] == 6
    assert game.cubes["green"] == 2
    assert game.cubes["red"] == 4
    assert game.gameNo == 1
    assert game.isPossible(limits) == True
    
    game = CubeGame(games[2])
    assert game.cubes["blue"] == 6
    assert game.cubes["green"] == 13
    assert game.cubes["red"] == 20
    assert game.gameNo == 3
    assert game.isPossible(limits) == False

def test_game_possibleSum():
    assert possibleSum(games, limits) == 8
    inputData = open("../data/input02.txt", "r")
    assert possibleSum(inputData, limits) == 1867
    
def test_game_powerSum():
    assert CubeGame(games[0]).power == 48
    assert CubeGame(games[1]).power == 12
    assert CubeGame(games[2]).power == 1560
    assert CubeGame(games[3]).power == 630
    assert CubeGame(games[4]).power == 36
    
    assert powerSum(games) == 2286
    inputData = open("../data/input02.txt", "r")
    assert powerSum(inputData) == 84538
