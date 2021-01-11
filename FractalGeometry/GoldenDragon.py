import turtle as t 
import math as m 
# from Tkinter import *


def heighway(depth, size, parity, par):
    phi=(1.0+m.sqrt(5.0))/2.0
    r=(1.0/phi)**(1.0/phi)
    a=m.degrees(m.acos((1.0+r**2-r**4)/(2.0*r)))
    b=m.degrees(m.acos((1.0+r**4-r**2)/(2.0*r**2)))
    c=[a,b]
    i=0
    if depth==0:
        if par%2==0:
            t.forward(size*r)           
        else:
            t.forward(size*r**2.0)
    else:
        t.left(parity*c[i%2]/2.0)
        #t.begin_fill()
        heighway (depth=depth-1, size=size/phi, parity=1, par=2)
        i+=1
        t.right(parity*(180-a-b))
        heighway (depth=depth-1, size=size/phi, parity=-1, par=1)
        i+=1
        #t.end_fill()
        t.left(parity*c[i%2]/2.0)
        

t.ht()
t.speed(2000)
origin=t.pos()
heading=t.heading()

j=0
d=4
s=200
p=1
arms=1
#phi=(1.0+m.sqrt(5))/2.0
#factor=(1.0/phi)**(1.0/phi)
color=["red", "yellow", "green", "blue"]


while j <=(arms-1):
        t.setposition(origin)
        t.seth(heading+(360.0/arms)*j)
        t.pencolor(color[j%len(color)])
        t.fillcolor(t.pencolor())
        #t.begin_fill()
        t.pendown()
        heighway(depth=d, size=s, parity=p, par=d)
        t.penup()
        #t.end_fill()
        j+=1

ts=t.getcanvas()
ts.postscript(file="GoldenTile.ps", colormode="color") 
t.done()     