from graphics import *
from Button import *

def main():


    win = GraphWin("Character Creator", 800, 800)
    Face = Oval(Point(100,100), Point(500,500))
    Face.draw(win)

    qB = Button(win, Point(700, 700), Point(800, 800), "red", "Quit")
    b = Button(win, Point(600, 300), Point(700, 375), "red", "Nose")
    b2 = Button(win, Point(600, 100), Point(700, 175), "cyan", "Left Eye")
    b3 = Button(win, Point(600, 200), Point(700, 275), "green", "Right Eye")
    b4 = Button(win, Point(600, 400), Point(700, 475), "yellow", "Mouth")
    b5 = Button(win, Point(600, 500), Point(700, 575), "orange", "Erase All")
    b6 = Button(win, Point(100, 600), Point(200, 675), "red", "Fill All Red")
    b7 = Button(win, Point(250, 600), Point(350, 675), "blue", "Fill All Blue")
    b8 = Button(win, Point(400, 600), Point(500, 675), "green", "Fill All Green")

    tNose = Polygon([Point(275, 350), Point(325, 250), Point(375, 350)])
    lEye = Oval(Point(400, 200), Point(450, 300))
    rEye = Oval(Point(200, 200), Point(250, 300))
    mMouth = Oval(Point(435, 385), Point(235, 435))

    stuff = [tNose, lEye, rEye, mMouth]

    while True:
    
        m = win.getMouse()
        if b.isClicked(m):
            #for e in stuff:
                #e.undraw()
                #e.setFill(red, blue, etc...)
            tNose.draw(win)

        elif b2.isClicked(m):
            #for e in stuff:
                #e.undraw()

            lEye.draw(win)

        elif b3.isClicked(m):
            #for e in stuff:
                #e.undraw()

            rEye.draw(win)

        elif b4.isClicked(m):
            #for e in stuff:
                #e.undraw()

            mMouth.draw(win)

        elif b5.isClicked(m):
            for e in stuff:
                e.undraw()

        elif b6.isClicked(m):
            for e in stuff:
                e.setFill("red")

        elif b7.isClicked(m):
            for e in stuff:
                e.setFill("blue")

        elif b8.isClicked(m):
            for e in stuff:
                e.setFill("green")

        elif qB.isClicked(m):
            break

    win.close()

        



    

if __name__ == "__main__":
    main()
