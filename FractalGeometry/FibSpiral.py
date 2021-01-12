import math as m
import turtle as t

a = 0e-5
b = 1e-5
c = 1e-5
iter = 0
phi = (1+m.sqrt(5))/2
rat = (c/b)
colors = ["black","red","orange","yellow","green","blue"]
#print ("Number: "+str(a).rjust(10)+"     Ratio: "+str(rat).rjust(10))
#print ("Number: "+str(b).rjust(10)+"     Ratio: "+str(rat).rjust(10))
#print ("Number: "+str(c).rjust(10)+"     Ratio: "+str(rat).rjust(10))

t.pendown()
t.ht()
for i in range(0,3):
    t.left(90)
    t.forward(c)

while (abs(phi-rat)>10**-20):
    iter+=1
    a = b
    b = c
    c = a+b
    t.pencolor(colors[iter%6])
    for i in range(0,4):
        t.forward(c)
        t.left(90)
    t.circle(c,90)
    rat = (c/b)
    print("Number: "+str(c).rjust(10)+"     Ratio: "+str(rat).rjust(10))
#    print ("Iteration: "+str(iter))
#    print ("A: "+str(a)+"  B: "+str(b)+"   Ratio: "+str(rat))
