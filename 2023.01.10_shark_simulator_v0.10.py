#Shark Simulator v0.10

from time import sleep
from random import randint
from graphics import *
from Button import *
from fish import *
from shark import *


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

def pos_to_point(pos):
    return Point((pos.getX()-1)*20+20, (pos.getY()-1)*20+20)

def point_to_pos(p):
    return Position((p.getX()-20)/20+1, (p.getY()-20)/20+1)

def pos_to_center(pos):
    return Point((pos.getX()-1)*20+30, (pos.getY()-1)*20+30)

def move(fish_objects, shark_object):
    f_objs, s_obj = fish_objects, shark_object
    fish_positions = []
    for i in fish_objects:
        fish_positions.append(i.getPos())
    s_obj.setPos(s_obj.move(fish_positions))
    for i in f_objs:
        i.setPos(i.move(fish_positions, s_obj.getPos()))
    return f_objs, s_obj

def main():
    window = GraphWin("Shark Simulator", 600, 600)
    for i in range(1, 22):
        l = Line(pos_to_point(Position(i, 1)), pos_to_point(Position(i, 21)))
        l.setWidth(2)
        l.draw(window)
    for i in range(1, 22):
        l = Line(pos_to_point(Position(1, i)), pos_to_point(Position(21, i)))
        l.setWidth(2)
        l.draw(window)
    button_move = Button(window, Point(440, 45), Point(580, 95), 2, "Move", "cyan", "black", "black")
    button_complete = Button(window, Point(440, 145), Point(580, 195), 2, "Complete", "cyan", "black", "black")
    button_reset = Button(window, Point(440, 245), Point(580, 295), 2, "Reset", "cyan", "black", "black")
    button_quit = Button(window, Point(440, 345), Point(580, 395), 2, "Quit", "tomato", "black", "black")
    button_move.draw()
    button_complete.draw()
    button_reset.draw()
    button_quit.draw()
    game_complete = False
    fishes = [Fish(Position(randint(1,20), randint(1,20)), Image(pos_to_center(Position(0, 0)), "fish_image.png")), Fish(Position(randint(1,20), randint(1,20)), Image(pos_to_center(Position(0, 0)), "fish_image.png")), Fish(Position(randint(1,20),randint(1,20)), Image(pos_to_center(Position(0, 0)), "fish_image.png"))]
    shark = Shark(Position(randint(1,20),randint(1,20)), Image(pos_to_center(Position(0, 0)), "shark_image.png"))
    #draw
    for i in fishes:
        i.setImage(Image(pos_to_center(i.getPos()), "fish_image.png"))
        i.getImage().draw(window)
    #line 66
    shark.setImage(Image(pos_to_center(shark.getPos()), "shark_image.png"))
    shark.getImage().draw(window)
    while(True):
        click = window.getMouse()
        if(button_move.isClick(click)):
            if(not(game_complete)):
                fishes, shark = move(fishes, shark)
                #undraw then draw
                for i in fishes:
                    i.getImage().undraw()
                    i.setImage(Image(pos_to_center(i.getPos()), "fish_image.png"))
                    i.getImage().draw(window)
                shark.getImage().undraw()
                shark.setImage(Image(pos_to_center(shark.getPos()), "shark_image.png"))
                shark.getImage().draw(window)
                #eat and check for completion
                fishes_2 = []
                for i in fishes:
                    if(i.getPos() != shark.getPos()):
                        fishes_2.append(i)
                fishes = fishes_2
                game_complete = (len(fishes) == 0)
        elif(button_reset.isClick(click)):
            for i in fishes:
                    i.getImage().undraw()
            shark.getImage().undraw()
            fishes = [Fish(Position(randint(1,19), randint(1,19)), Image(pos_to_center(Position(0, 0)), "fish_image.png")), Fish(Position(randint(1,19), randint(1,19)), Image(pos_to_center(Position(0, 0)), "fish_image.png")), Fish(Position(randint(1,19),randint(1,19)), Image(pos_to_center(Position(0, 0)), "fish_image.png"))]
            shark = Shark(Position(randint(1,19),randint(1,19)), Image(pos_to_center(Position(0, 0)), "shark_image.png"))
            #draw
            for i in fishes:
                i.setImage(Image(pos_to_center(i.getPos()), "fish_image.png"))
                i.getImage().draw(window)
            shark.setImage(Image(pos_to_center(shark.getPos()), "shark_image.png"))
            shark.getImage().draw(window)
        elif(button_complete.isClick(click)):
            while(not(game_complete)):
                fishes, shark = move(fishes, shark)
                game_complete = (len(fishes) == 0)
                for i in fishes:
                    i.getImage().undraw()
                    i.setImage(Image(pos_to_center(i.getPos()), "fish_image.png"))
                    i.getImage().draw(window)
                shark.getImage().undraw()
                shark.setImage(Image(pos_to_center(shark.getPos()), "shark_image.png"))
                shark.getImage().draw(window)
                '''fishes, shark = move(fishes, shark)
                #eat and check for completion
                fishes_2 = []
                for i in fishes:
                    if(i.getPos() != shark.getPos()):
                        fishes_2.append(i)
                fishes = fishes_2
                game_complete = (len(fishes) == 0)'''
            #undraw then draw
            for i in fishes:
                i.getImage().undraw()
                i.setImage(Image(pos_to_center(i.getPos()), "fish_image.png"))
                i.getImage().draw(window)
            shark.getImage().undraw()
            shark.setImage(Image(pos_to_center(shark.getPos()), "shark_image.png"))
            shark.getImage().draw(window)
        elif(button_quit.isClick(click)):
            window.close()
            exit()
        game_complete = (len(fishes) == 0)

if(__name__ == "__main__"):
    main()
