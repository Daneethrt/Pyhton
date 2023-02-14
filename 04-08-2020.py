#Area of square as input and print as perimeter
import math
def squ(a):
    s=math.sqrt(a)
    p=4*s
    print(p)
squ(25)

#Area of circle as input and print circumference of circle.
import math
def cir(area):
    radius=math.sqrt(area/math.pi)
    circumference=2*math.pi*radius
    print(circumference)

cir(20)

import math
def clin(r,h):
    TSA=2*math.pi*r*(r+h)
    v=math.pi*math.sqrt(r)*h
    print('TSA is',TSA,'volume is',v)

clin(1,2)

