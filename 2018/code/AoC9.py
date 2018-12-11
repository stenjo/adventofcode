# Advent of Code 2018: https://adventofcode.com/2018/day/9
# 
# 

import unittest
import datetime, time
from datetime import timedelta
import pprint
import collections

DEBUG = True

start = datetime.datetime.now()
pp = pprint.PrettyPrinter(width=180, compact=True)

inputData = open('../data/input9.txt','r')
testData = [
            '20 players; last marble is worth 75000 points: high score is 112',
            '4 players; last marble is worth 100 points: high score is 107',
            '5 players; last marble is worth 125 points: high score is 165',
            '8 players; last marble is worth 100 points: high score is 107',
            '9 players; last marble is worth 200 points: high score is 227',
            '10 players; last marble is worth 1618 points: high score is 8317',
            '13 players; last marble is worth 7999 points: high score is 146373',
            '17 players; last marble is worth 1104 points: high score is 2764',
            '21 players; last marble is worth 6111 points: high score is 54718',
            '30 players; last marble is worth 5807 points: high score is 37305',
            '9 players; last marble is worth 25 points: high score is 37305']
liveData = [inputData.readline().strip()]

def getPlayersAndWorth(line):
    parts = line.split(' ')
    return [parts[0], parts[6]]
    
if DEBUG:
    inData = [getPlayersAndWorth(d) for d in testData]
    # inData = testData2
else:
    inData = [getPlayersAndWorth(d) for d in liveData]


# if DEBUG:
#     pp.pprint(inData)

class Ball():
    value = 0
    def __init__(self, value):
        self.value = value

class Player():
    score = 0
    index = 0
    def __init__(self, index):
        self.score = 0
        self.index = index + 1


class Circle():
    circle = []
    current = 0

    def insert(self, ball):
        if ball.value % 23 == 0 and len(self.circle) > 0:
            self.current = (self.current-7) % len(self.circle)
            return ball.value + self.circle.pop((self.current-7) % len(self.circle)).value
        elif len(self.circle) > 0:
            self.circle.insert((self.current+2) % len(self.circle))
            self.current = self.circle.index(ball)
        return 0

    def remove(self, index):
        return self.circle.pop(index).value

class Game():
    
    c = Circle()
    balls = []
    players = []

    def __init__(self, data):
        self.initialize(data)

    def initialize(self, data):
        self.balls = [Ball(i) for i in range(0,int(data[1])+1)]
        self.players = [Player(i) for i in range(int(data[0]))]

    def runGame(self):

        player = self.players[0]
        self.c.insert(self.balls.pop(0))
        self.printCircle(Player(-1))
        for ball in self.balls:
            player.score += self.c.insert(ball)
            self.printCircle(player)
            player = self.players[player.index % len(self.players)]

        return [p.score for p in self.players]

    def printCircle(self, player):
        if player.index == 0:
            s = ('[-]').rjust(4)
        else:
            s = ('['+str(player.index)+']').rjust(4)

        for n in self.c.circle:
            if self.c.circle.index(n) == self.c.current:
                s += ('(' + str(n.value) + ')').rjust(4)
            else:
                s += (str(n.value).rjust(3) + ' ')
        print(s)

exit(1)
g = Game(inData[1])
print([b.value for b in g.balls])
print([p.index for p in g.players])
print(g.runGame())
exit(0)

### PART 1 ###
def printMarbles(player, current, circle):
    if player == '-':
        s = ('[-]').rjust(4)
    else:
        s = ('['+str(int(player) + 1)+']').rjust(4)

    for n in circle:
        if circle.index(n) == current:
            s += ('(' + str(n) + ')').rjust(4)
        else:
            s += (str(n).rjust(3) + ' ')
    print(s)

def runGame(params):
    print(params)
    balls = [i for i in range(0,int(params[1])+1)]
    players = int(params[0])
    circle = []
    current = 0
    scores = [ 0 for i in range(players)]
    # printMarbles('-', current, circle)
    while len(balls) > 0:
        for p in range(players):
            if len(balls):
                ball = balls.pop(0)
                if len(circle) > 1 and current+2 != len(circle):
                    if ball % 23 == 0:   #Marble is divisble by 23
                        scores[p-1] += ball
                        pos = (current-7) % len(circle)
                        scores[p-1] += circle.pop(pos)
                        current = pos
                    else:
                        circle.insert( (current+2) % len(circle), ball)
                        current = circle.index(ball)
                else:
                    # if current+2 == len(circle):
                    #     print(p, current, len(circle))
                    circle.append(ball)
                    current = circle.index(ball)

                # if current == 0 and p != 0:    
                #     printMarbles(p, current, circle)

                # if p == 30:
                #     exit()

    # print(scores)
    print('Part 1: The winning elfs score is:', max(scores), '\n')


for params in inData:
    runGame(params)

### PART 2 ###


# print('\nPart 2: the value of the root node is:',sum)


end = datetime.datetime.now()
duration = end-start
print('Completed in',duration.seconds, 'seconds and', duration.microseconds/1000,'ms\n')
