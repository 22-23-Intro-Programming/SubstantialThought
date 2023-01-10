#fish

from math import sqrt
from random import randint, choice
from graphics import *

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __repr__(self):
        return "Position({}, {})".format(self.x, self.y)
    def __eq__(self, pos):
        return self.x == pos.x and self.y == pos.y
    def __ne__(self, pos):
        return self.x != pos.x and self.y != pos.y
    def getX(self):
        return self.x
    def getY(self):
        return self.y

def _dist(pos1, pos2):
    return sqrt(((pos1.getX() - pos2.getX()) ** 2) + ((pos1.getY() - pos2.getY()) ** 2))

class Fish:
    def __init__(self, pos, image):
        self.pos = pos
        self.image = image
    def __repr__(self):
        return "Fish({}, {})".format(self.pos, self.image)
    def getPos(self):
        return self.pos
    def setPos(self, pos):
        self.pos = pos
    def getImage(self):
        return self.image
    def setImage(self, image):
        self.image = image
    def getValidMoves(self, fish_positions):
        valid_moves = []
        for i in range(-1, 1):
            for j in range(-1, 1):
                valid_moves.append(Position(self.pos.getX() + i, self.pos.getY() + j))
        valid_moves_2 = []
        for i in valid_moves:
            if(1 <= i.getX() <= 20 and 1 <= i.getY() <= 20 and not(i in fish_positions) and i != self.pos):
                valid_moves_2.append(i)
        return valid_moves_2
    def move(self, fish_positions, shark_position):
        valid_moves = self.getValidMoves(fish_positions)
        if(valid_moves == []):
            return self.pos
        valid_moves = self.getValidMoves(fish_positions)
        if(_dist(self.pos, shark_position) >= 6):
            return choice(valid_moves)
        else:
            move_scores = []
            for i in valid_moves:
                move_scores.append({"score": _dist(i, shark_position), "move": i})
            move_scores.sort(key = lambda x: x["score"], reverse = True)
            print(valid_moves, move_scores)
            print(move_scores[0]["move"])
            return move_scores[0]["move"]
