import numpy as np
import turtle as t
import math

class TurtleFractal():
    """
    A class which is capable of drawing many kinds of fractals 
    using the Python Turtle package.

    """

    def __init__(self,show_turtle=False):
        t.speed(0)
        if show_turtle is not True:
            t.ht()
        t.seth(90)
        self.heading = t.heading()
        self.origin = t.pos()
        # t.exitonclick()
        return


    def BarnsleyFern(self):
        """
        Draws the Barnsley Fern.
        """

        prob=[.01,.85,.07,.07]
        ifs=[[[0.00,0.00],[0.00,0.16]],
            [[0.85,0.04],[-.04,.85]],
            [[0.20,-.26],[0.23,0.22]],
            [[-.15,0.28],[0.26,0.24]]]
        oth=[[0,0],[0,1.6],[0,1.6],[0,.44]]

        t.setworldcoordinates(-2.2,0,2.7,10.2)
        t.penup()
        t.hideturtle()
        t.color("dark green")
        t.speed(0)

        i=0
        while i<10**5:
            t.dot(3)
            func=np.random.choice(len(prob),p=prob)
            position=np.dot(ifs[func],t.position())+oth[func]
            t.setpos(position)
            if i%100==0:
                print (i)
            i+=1

        print ("done")
        ts=t.getcanvas()
        ts.postscript(file="BarnsFern.ps", colormode="color")

        t.exitonclick()


    def BarnsleyLeaf(self, depth=10, size=100, top=True):
        """
        Draws the Barnsley Leaf. 

        """
        # if top==True:
        #     t.left(90)
        if depth<1:
            t.forward(2.0*size)
            # t.penup()
            t.back(2.0*size)
            # t.pendown()
        else:
            t.forward(size)
            self.BarnsleyLeaf(depth=depth-2, size=size/2.0,top=False)
            # t.penup()
            t.back(size)
            # t.pendown()
            t.left(45)
            self.BarnsleyLeaf(depth=depth-1,size=size/math.sqrt(2),top=False)
            t.right(90)
            self.BarnsleyLeaf(depth=depth-1,size=size/math.sqrt(2),top=False)
            t.left(45)


    def HeighwayDragon(self, depth=12, size=200, parity=1,factor=1/math.sqrt(2)):
        if depth==0:
            t.forward(size)
        else:
            t.left(parity*45)
            self.HeighwayDragon(depth=depth-1, size=size*factor, parity=1)
            t.right(parity*90)
            self.HeighwayDragon (depth=depth-1, size=size*factor, parity=-1)
            t.left(parity*45)


    def HeighwayPinwheel(self,):

        num_arms = 4
        # heading = self.heading
        for i in range(num_arms):
            t.setposition(self.origin)
            t.seth(self.heading+(360.0/num_arms)*i)
            t.pendown()
            self.HeighwayDragon(depth=6)
            t.penup()


    def SierpinskiDragon(self, depth=8, size=200, parity=1):
        if depth == 0:
            t.forward(size)
        else:
            t.left(60*parity)
            self.SierpinskiDragon(depth=depth-1, size=size/2, parity=-parity)
            t.right(60*parity)
            self.SierpinskiDragon(depth=depth-1, size=size/2, parity=parity)
            t.right(60*parity)
            self.SierpinskiDragon(depth=depth-1, size=size/2, parity=-parity)
            t.left(60*parity)


    def Pentadendrite(self, depth=5,size=200,offangle=11.82, shrink=1/2.87):
        if depth==0:
            t.forward(size)
        else:
            t.left(offangle)
            self.Pentadendrite(depth=depth-1, size=size*shrink)
            t.left(72)
            self.Pentadendrite(depth=depth-1, size=size*shrink)
            t.right(72)
            self.Pentadendrite(depth=depth-1, size=size*shrink)
            t.right(144)
            self.Pentadendrite(depth=depth-1, size=size*shrink)
            t.left(72)
            self.Pentadendrite(depth=depth-1, size=size*shrink)
            t.left(72)
            self.Pentadendrite(depth=depth-1, size=size*shrink)
            t.right(offangle)


    def EisensteinBoundary(self, depth=6, size=200, parity=1):
        self.EBForward(depth=depth, size=size, parity=parity)
        self.EBBackwards(depth=depth, size=size, parity=parity)

    def EBForward(self, depth=10, size=200, parity=1):
        if depth == 0:
            t.forward(size)
        else:
            t.left(60*parity)
            self.EBBackwards(depth=depth-1, size=size/2, parity=-parity)
            t.right(120*parity)
            self.EBForward(depth=depth-1, size=size/2, parity=parity)
            t.left(60*parity)
            self.EBForward(depth=depth-1, size=size/2, parity=-parity)

    def EBBackwards(self, depth=10, size=200, parity=1):
        if depth == 0:
            t.forward(size)
        else:
            self.EBBackwards(depth=depth-1, size=size/2, parity=-parity)
            t.right(60*parity)
            self.EBBackwards(depth=depth-1, size=size/2, parity=parity)
            t.left(120*parity)
            self.EBForward(depth=depth-1, size=size/2, parity=-parity)
            t.right(60*parity)


    def KochCurve(self, depth=6, size=200):
        if depth == 0:
            t.forward(size)
        else:
            self.KochCurve(depth=depth-1, size=size/3)
            t.left(60)
            self.KochCurve(depth=depth-1, size=size/3)
            t.right(120)
            self.KochCurve(depth=depth-1, size=size/3)
            t.left(60)
            self.KochCurve(depth=depth-1, size=size/3)


def main():
    tf = TurtleFractal()
    tf.KochCurve()
    t.exitonclick()


if __name__ == '__main__':
    main()
    
