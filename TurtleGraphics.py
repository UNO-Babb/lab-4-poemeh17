#TurtleGraphics.py
#Name:
#Date:
#Assignment:

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(bob, sides):
    for s in range(sides):
        bob.forward(50)
        bob.right(360/sides)
        
def fillCorner(alice, corner):
    #draw a big square
    drawSquare(alice, 100)
    
    if corner == 1:
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
    elif corner == 2:
        alice.forward(50)
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
    if corner == 3:
        alice.forward(100)
        alice.right(90)
        alice.forward(100)
        alice.right(90)
        alice.forward(50)
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
    if corner == 4:
        alice.forward(100)
        alice.right(90)
        alice.forward(50)
        alice.begin_fill()
        drawSquare(alice, 50)
        alice.end_fill()
        
def squaresInSquares(lily, squares):
    if squares == 5:
        drawSquare(lily, 150)
        lily.up()
        lily.forward(140)
        lily.right(90)
        lily.forward(10)
        lily.down()
        drawSquare(lily, 130)
        lily.up()
        lily.forward(120)
        lily.right(90)
        lily.forward(10)
        lily.down()
        drawSquare(lily, 110)
        lily.up()
        lily.forward(100)
        lily.right(90)
        lily.forward(10)
        lily.down()
        drawSquare(lily, 90)
        lily.up()
        lily.forward(80)
        lily.right(90)
        lily.forward(10)
        lily.down()
        drawSquare(lily, 70)
    if squares == 3:
        drawSquare(lily, 100)
        lily.up()
        lily.forward(90)
        lily.right(90)
        lily.forward(10)
        lily.down()
        drawSquare(lily, 80)
        lily.up()
        lily.forward(70)
        lily.right(90)
        lily.forward(10)
        lily.down()
        drawSquare(lily, 60)
    

        

def main():
    myTurtle = turtle.Turtle()
    
    # drawSquare(myTurtle, 100)
    
    #drawPolygon(myTurtle, 5) #draws a pentagon
    #drawPolygon(myTurtle, 8) #draws an octogon
    #drawPolygon(myTurtle, 3)
   
    #fillCorner(myTurtle, 1)
    #fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    #fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.
    #fillCorner(myTurtle, 4)

    #squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    #squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()
