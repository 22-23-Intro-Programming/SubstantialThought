from graphics import*
from Button import*

def darken(img):

    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            r, g, b = pix[0], pix[1], pix[2]


            r = r - 50
            g = g - 50
            b = b - 50

            if r <= 0:
                r = 0
            if g <= 0:
                g = 0
            if b <= 0:
                b = 0

            
            newColor = color_rgb(r, g, b)
            img.setPixel(i, j, newColor)

def lighten(img):

    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            r, g, b = pix[0], pix[1], pix[2]


            r = r + 50
            g = g + 50
            b = b + 50

            if r >= 255:
                r = 255
            if g >= 255:
                g = 255
            if b >= 255:
                b = 255

            
            newColor = color_rgb(r, g, b)
            img.setPixel(i, j, newColor)

def grayScale(img):

    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            r, g, b = pix[0], pix[1], pix[2]


            avg = ((r + g + b) / 3)

            r = int(r)
            g = int(g)
            b = int(b)
            avg = int(avg)

            newColor = color_rgb(avg, avg, avg)
            img.setPixel(i, j, newColor)

def contrast(img):

    x = img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            pix = img.getPixel(i, j)
            r, g, b = pix[0], pix[1], pix[2]

            if r <= 150:
                if g <= 150:
                    if b <= 150:
                        r = r - 30
                        b = r - 30
                        g = r - 30

            if r >= 150:
                if g >= 150:
                    if b >= 150:
                        r = r + 30
                        b = b + 30
                        g = g + 30


            if r >= 255:
                r = 255
            if g >= 255:
                g = 255
            if b >= 255:
                b = 255

            if r <= 0:
                r = 0
            if g <= 0:
                g = 0
            if b <= 0:
                b = 0
                
            newColor = color_rgb(r, g, b)
            img.setPixel(i, j, newColor)
    

def main():

    #I used Mr. Considine's image for this project
    
    win = GraphWin("Image Editor", 1000, 1000)
    win.setBackground("#edff90")

    I = Image(Point(400, 400), "veitchii.png")
    I.draw(win)

    B = Button(win, Point(700, 200), Point(800, 275), "#3b3b3b", "Darken")
    B2 = Button(win, Point(700, 300), Point(800, 375), "#ffffff", "Lighten")
    B3 = Button(win, Point(700, 400), Point(800, 475), "#827d80", "Grayscale")
    B4 = Button(win, Point(700, 500), Point(800, 575), "#ff0091", "Contrast")
    B5 = Button(win, Point(700, 100), Point(800, 175), "#00ffc7", "Original")
    Q = Button(win, Point(700, 600), Point(800, 675), "tomato", "Quit")

    while True:
        m = win.getMouse()
        
        if B.isClicked(m):
            darken(I)
            
        if B2.isClicked(m):
            lighten(I)

        if B3.isClicked(m):
            grayScale(I)

        if B4.isClicked(m):
            contrast(I)
            
        if B5.isClicked(m):
            
            I.undraw()
            I = Image(Point(400, 400), "veitchii.png")
            I.draw(win)

        if Q.isClicked(m):
            break

    win.close()

if __name__ == "__main__":
    main()
