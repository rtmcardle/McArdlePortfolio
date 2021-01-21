###############################################################
####    
####    Ryan McArdle
####    Original: Spring 2016
####    Refresh: January 2021
####
####    A class which utilizes Turtle Graphics to draw various
####    fractal images. Most algorithms borrowed from "Measure,
####    Topology, and Fractal Geometry" by Gerald Edgar, 
####    Springer Publishing, 2nd ed, 2008. These algorithms 
####    were studied as a part of a directed reading course
####    focusing on fractal geometry.
####
###############################################################

from PIL import Image
import turtle as t
import numpy as np
import io, math, os

class TurtleFractal():
    """
    A class which is capable of drawing many kinds of fractals 
    using the Python Turtle package.

    """

    def __init__(self,show_turtle=False):
        self.setTurtle()
        return


    def setTurtle(self,show_turtle=False,heading=90):
        """
        Sets the Turtle to the origin with a clear screen, then
        sets speed to max, hides Turtle, and orients the Turtle
        to the heading. Called after each image is saved.

        :param show_turtle: whether to show the Turtle or not. 
            Default to False to optimize speed of drawings.
        :param heading: the initial orientation of the Turtle.
            90 = North, 0 = East.
        """

        t.resetscreen()
        t.speed(0)
        if show_turtle is not True:
            t.ht()
        t.seth(heading)
        self.heading = t.heading()
        self.origin = t.pos()


    def BarnsleyFern(self,dots=10**5):
        """
        Draws the Barnsley Fern using an Iterated Function 
        System and a stipling technique. Turtle draws a dot at 
        its location, then randomly selects a transformation 
        from the IFS to choose a new position and draw another 
        dot. Upon repetition, the Fern is drawn.

        :param dots: the number of dots to generate in the 
            image
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
        choices = len(prob)
        while i<dots:
            t.dot(3)
            func=np.random.choice(choices,p=prob)
            position=np.dot(ifs[func],t.position())+oth[func]
            t.setpos(position)
            #if i%100==0:
            #    print (i)
            i+=1

        print ("done")


    def BarnsleyLeaf(self, depth=10, size=100):
        """
        Draws the Barnsley Leaf. This one may be worth viewing
        with Turtle visible, as the definition leads to 
        considerable backtracking and rotating in place.

        :param depth: the number of recursive calls to be made
        :param size: the base size of the leaf
        """

        if depth<1:
            t.forward(2.0*size)
            t.back(2.0*size)
        else:
            t.forward(size)
            self.BarnsleyLeaf(depth=depth-2, size=size/2.0)
            t.back(size)
            t.left(45)
            self.BarnsleyLeaf(depth=depth-1,size=size/math.sqrt(2))
            t.right(90)
            self.BarnsleyLeaf(depth=depth-1,size=size/math.sqrt(2))
            t.left(45)


    def HeighwayDragon(self, depth=12, size=200, parity=1,factor=1/math.sqrt(2)):
        """
        Draws the Heighway Dragon. This dragon can be 
        approximated by drawing a line segment, then 
        iteratively replacing line segments with the two 
        short legs of a 45-45-90 triangle in alternating 
        directions. This non-self-intersecting curve can be 
        combined with copies of itself to tile the plane (see 
        HeighwayPinwheel()).

        :param depth: the number of recursive calls to be made
        :param size: the base size of the dragon
        :param parity: tracks alternations in the recursive 
            calls; changes direction of turns
        :param factor: an overall scaling factor
        """
        if depth==0:
            t.forward(size)
        else:
            t.left(parity*45)
            self.HeighwayDragon(depth=depth-1, size=size*factor, parity=1)
            t.right(parity*90)
            self.HeighwayDragon (depth=depth-1, size=size*factor, parity=-1)
            t.left(parity*45)


    def HeighwayPinwheel(self,depth=6,size=200):
        """
        Draws four Heighway Dragons radiating from the origin.
        These dragons will never intersect, and in the limit 
        that depth -> inf and size -> inf, the curve fills the 
        plane.

        :param depth: the number of recursive calls to be made
        :param size: the base size of each dragon
        """

        num_arms = 4
        for i in range(num_arms):
            t.setposition(self.origin)
            t.seth(self.heading+(360.0/num_arms)*i)
            t.pendown()
            self.HeighwayDragon(depth,size)
            t.penup()


    def SierpinskiDragon(self, depth=8, size=200, parity=1):
        """
        Draws the Sierpinski Dragon. Similar to the Heighway 
        Dragon, can be approximated with a line segment, then
        iteratively replacing line segments with one-half of a 
        hexagon that would span the length of the segment, 
        alternating directions. In the limit that depth -> inf,
        the curve approximates the Sierpinski Gasket.

        :param depth: the number of recursive calls to be made
        :param size: the base size of the dragon
        :param parity: tracks alternations in the recursive 
            calls; changes direction of turns
        """

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


    def SierpinskiGasket(self,depth=9,size=200):
        """
        Rotates the Turtle so that SierpinskiDragon() draws a 
        properly oriented Sierpinski Gasket.

        :param depth: the number of recursive calls to be made
        :param size: the base size of the dragon
        """

        t.left(30)
        t.penup()
        t.setposition(size,-size*2/3)
        t.pendown()
        for _ in range(1):
            self.SierpinskiDragon(depth=depth+1,size=800)
            t.right(120)


    def McWortersPentigree(self, depth=5,size=200,offangle=11.82, shrink=1/2.87):
        """
        Draws a variation on McWorter's Pentigree. Setting 
        offangle = 36 and shrink = (3 + sqrt(5))/2 will 
        generate the original pentigree. The default parameters
        set here allow for the creation of the Pentadendrite.

        :param depth: the number of recursive calls
        :param size: the base size of the pentigree
        :param offangle: an initial and final rotation angle 
            for each recursive call
        :param shrink: a scale factor between recursive calls
        """

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
        """
        Draws five copies of the defined variation of 
        McWorter's Pentigree in a radial fashion to create the 
        'Pentadendrite' pattern.

        :param depth: the number of recursive calls to be made
        :param size: the base size of each pentigree.
        """

        t.penup()
        t.setposition(size/(2*math.tan(math.pi/5)),-size/2)
        t.pendown()
        for _ in range(5):
            self.McWortersPentigree(depth,size)
            t.left(360//5)


    def EisensteinBoundary(self, depth=6, size=200, parity=1):
        """
        Draws a portion of the boundary of the Eisenstein 
        iterated function system.

        :param depth: the number of recursive calls to be made
        :param size: the base size of the boundary
        :param parity: tracks alternations in the recursive 
            calls; changes direction of turns
        """
        self.EBForward(depth=depth, size=size, parity=parity)
        self.EBBackwards(depth=depth, size=size, parity=parity)


    def EBForward(self, depth=10, size=200, parity=1):
        """
        Support function for drawing the Eisenstein Boundary.

        :param depth: the number of recursive calls to be made
        :param size: the base size of the boundary
        :param parity: tracks alternations in the recursive 
            calls; changes direction of turns
        """

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
        """
        Support function for drawing the Eisenstein Boundary.

        :param depth: the number of recursive calls to be made
        :param size: the base size of the boundary
        :param parity: tracks alternations in the recursive 
            calls; changes direction of turns
        """

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
        """
        Draws the full Eisenstein Boundary from six portions.

        :param depth: the number of recursive calls to be made
        :param size: the base size of the boundary
        """

        t.penup()
        t.setposition(math.sqrt(3)*size,-size)
        t.pendown()
        for _ in range(6):
            self.EisensteinBoundary(depth, size)
            t.left(60)


    def KochCurve(self, depth=6, size=200):
        """
        Draws the Koch Curve. This curve is approximated by 
        drawing a line, then replacing the middle third of the
        line with two sides of an equilateral triangle, and 
        iteratively repeating. This curve is used to create 
        KochSnowFlake().

        :param depth: the number of recursive calls to be made
        :param size: the base size of the boundary
        """

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
        """
        Draws three copies of the Koch Curve in order to create
        the boundary known as the Koch Snowflake. 

        :param depth: the number of recursive calls to be made
        :param size: the base size of the boundary
        """

        t.penup()
        t.setposition(-math.sqrt(3)*size/4,-size/2)
        t.pendown()
        for _ in range(3):
            self.KochCurve(depth,size)
            t.right(120)


    def FibonacciSpiral(self):
        """
        Approximates the Golden Ratio by calculating 
        Fibonacci Numbers and drawing a spiral based upon those
        values. Terminates when the computer can no longer 
        discern the approximated ratio from the value 
        (1+sqrt(5))/2.
        """

        iteration = 0
        a=0
        b=1
        c = a+b
        ratio = c/b
        phi = (1+math.sqrt(5))/2

        while (abs(phi-ratio)>0):
            scale = 0.01
            for i in range(0,4):
                t.forward(c*scale)
                t.left(90)
            t.circle(c*scale,90)
            ratio = (c/b)
            print("Number: "+str(c).rjust(10)+"     Ratio: "+str(ratio).rjust(10))
            iteration+=1
            a = b
            b = c
            c = a+b
          
            
    def saveImage(self,file_name):
        """
        Saves the current canvas as a .png image and resets the
        Turtle for another drawing.

        :param file_name: the name to save the file as
        """

        cur_dir = os.getcwd()
        rec_dir = os.path.join(cur_dir,'Images\\')
        if not os.path.exists(rec_dir):
            os.mkdir(rec_dir)
        ts=t.getcanvas()
        psimage = ts.postscript(file= file_name+'.ps', colormode="color")
        with Image.open(file_name+'.ps') as img:
            img.save(os.path.join(rec_dir,file_name+'.png'), 'png', dpi=(1000,1000))
        os.remove(file_name+'.ps')
        self.setTurtle()



def main():
    tf = TurtleFractal()

    depths = 8
    sizes = 400

    #tf.BarnsleyFern()
    #tf.saveImage('BarnsleyFern')

    #t.setpos(0,-275)
    #tf.BarnsleyLeaf(depth=depths+2, size=sizes)
    #tf.saveImage('BarnsleyLeaf')

    #tf.HeighwayPinwheel(depth=depths+4, size=sizes)
    #tf.saveImage('HeighwayPinwheel')

    ############
    #tf.SierpinskiDragon(depth=8, size=400)
    ############

    tf.SierpinskiGasket(depth=depths, size=sizes)
    tf.saveImage('SierpinskiGasket')

    #tf.Pentadendrite(depth=depths/2+2, size=sizes+100)
    #tf.saveImage('Pentadendrite')

    ###########
    #tf.EisensteinBoundaryFull(depth=4)
    #tf.saveImage('EisensteinBoundary')
    ##########

    #tf.KochSnowFlake(depth=6, size=400*1.5)
    #tf.saveImage('KochSnowFlake')

    ############
    #tf.FibonacciSpiral()
    #tf.saveImage('FibonacciSpiral')
    #############



if __name__ == '__main__':
    main()
    
