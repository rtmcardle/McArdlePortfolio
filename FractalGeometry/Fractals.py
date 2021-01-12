import numpy as np
import turtle as t
import math
import os, io
from PIL import Image

class TurtleFractal():
    """
    A class which is capable of drawing many kinds of fractals 
    using the Python Turtle package.

    """

    def __init__(self,show_turtle=False):
        self.setTurtle()
        return

    def setTurtle(self,show_turtle=False):
        t.speed(0)
        if show_turtle is not True:
            t.ht()
        t.seth(90)
        self.heading = t.heading()
        self.origin = t.pos()


    def BarnsleyFern(self,depth=10**5):
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
        while i<depth:
            t.dot(3)
            func=np.random.choice(len(prob),p=prob)
            position=np.dot(ifs[func],t.position())+oth[func]
            t.setpos(position)
            if i%100==0:
                print (i)
            i+=1

        print ("done")


    def BarnsleyLeaf(self, depth=10, size=100, top=True):
        """
        Draws the Barnsley Leaf. 

        """
        if depth<1:
            t.forward(2.0*size)
            t.back(2.0*size)
        else:
            t.forward(size)
            self.BarnsleyLeaf(depth=depth-2, size=size/2.0,top=False)
            t.back(size)
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


    def HeighwayPinwheel(self,depth=6,size=200):

        num_arms = 4
        for i in range(num_arms):
            t.setposition(self.origin)
            t.seth(self.heading+(360.0/num_arms)*i)
            t.pendown()
            self.HeighwayDragon(depth,size)
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

    def SierpinskiGasket(self,depth=8,size=200):
        t.right(90)
        t.penup()
        t.setposition(-size/2,size/2)
        t.pendown()
        for _ in range(3):
            self.SierpinskiDragon(depth,size)
            t.right(60)
            t.forward(size/(4*depth))
            t.right(60)



    def McWortersPentigree(self, depth=5,size=200,offangle=11.82, shrink=1/2.87):
        if depth==0:
            t.forward(size)
        else:
            t.left(offangle)
            self.McWortersPentigree(depth=depth-1, size=size*shrink)
            t.left(72)
            self.McWortersPentigree(depth=depth-1, size=size*shrink)
            t.right(72)
            self.McWortersPentigree(depth=depth-1, size=size*shrink)
            t.right(144)
            self.McWortersPentigree(depth=depth-1, size=size*shrink)
            t.left(72)
            self.McWortersPentigree(depth=depth-1, size=size*shrink)
            t.left(72)
            self.McWortersPentigree(depth=depth-1, size=size*shrink)
            t.right(offangle)

    def Pentadendrite(self, depth=5,size=200):
        t.penup()
        t.setposition(size/(2*math.tan(math.pi/5)),-size/2)
        t.pendown()
        for _ in range(5):
            self.McWortersPentigree(depth,size)
            t.left(360//5)


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

    def EisensteinBoundaryFull(self, depth=6, size=200):
        t.penup()
        t.setposition(math.sqrt(3)*size,-size)
        t.pendown()
        for _ in range(6):
            self.EisensteinBoundary(depth, size)
            t.left(60)


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

    def KochSnowFlake(self, depth=6, size=200):
        t.penup()
        t.setposition(-math.sqrt(3)*size/4,-size/2)
        t.pendown()
        for _ in range(3):
            self.KochCurve(depth,size)
            t.right(120)

    def saveImage(self,file_name):
        cur_dir = os.getcwd()
        rec_dir = os.path.join(cur_dir,'Images\\')
        if not os.path.exists(rec_dir):
            os.mkdir(rec_dir)
        ts=t.getcanvas()
        psimage = ts.postscript(file= file_name+'.ps', colormode="color")
        with Image.open(file_name+'.ps') as img:
            img.save(os.path.join(rec_dir,file_name+'.png'), 'png', dpi=(1000,1000))
        os.remove(file_name+'.ps')
        t.resetscreen()
        self.setTurtle()


def main():
    tf = TurtleFractal()

    depths = 8

    tf.BarnsleyFern()
    tf.saveImage('BarnsleyFern')

    tf.BarnsleyLeaf(depth=depths)
    tf.saveImage('BarnsleyLeaf')

    tf.HeighwayPinwheel(depth=depths)
    tf.saveImage('HeighwayPinwheel')

    tf.SierpinskiGasket(depth=depths)
    tf.saveImage('SierpinskiGasket')

    tf.Pentadendrite(depth=depths/2)
    tf.saveImage('Pentadendrite')

    tf.EisensteinBoundaryFull(depth=depths)
    tf.saveImage('EisensteinBoundaryFull')

    tf.KochSnowFlake(depth=depths)
    tf.saveImage('KochSnowFlake')


if __name__ == '__main__':
    main()
    
