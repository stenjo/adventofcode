
class CubeGame:
    def __init__(self, game):
        self.gameNo = 0
        self.cubes = {}
        gameStr,cubesStr = game.split(':')
        self.gameNo = int(gameStr.split(' ')[1])
        for gameSetStr in cubesStr[1::].strip().split(';'):
            for cubeStr in gameSetStr.strip().split(','):
                cubeCount,cubeColor = cubeStr.strip().split(' ')
                if cubeColor in self.cubes:
                    if int(cubeCount) > self.cubes[cubeColor]:
                        self.cubes[cubeColor] = int(cubeCount)
                else:
                    self.cubes[cubeColor] = int(cubeCount)
        self.power = self.cubes["red"]*self.cubes["green"]*self.cubes["blue"]
        
        
    def isPossible(self, limits:dict):
        for color, count in limits.items():
            if count < self.cubes[color]:
                return False
            
        return True
    
def possibleSum(games, limits):
    sum = 0
    for game in games:
        g = CubeGame(game)
        if g.isPossible(limits):
            sum += g.gameNo
            
    return sum

def powerSum(games):
    sum = 0
    for game in games:
        sum += CubeGame(game).power
            
    return sum
