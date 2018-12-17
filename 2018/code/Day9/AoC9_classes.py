# Advent of Code 2018: https://adventofcode.com/2018/day/9
# 
# 

import unittest
import datetime, time
from datetime import timedelta
import pprint
import collections


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

