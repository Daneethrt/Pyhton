#To volume and TSA of cubeiod.
import math
def cub(l,b,h):
    TSA=2*(l*b+b*h+h*l)
    v=l*b*h
    print('TSA of cubiod',TSA,'volume of cubiod',v)
cub(1,2,3)
#To volume and TSA of sphere
import math
def sph(r):
    TSA=4*math.pi*math.sqrt(r)
    v=4/3*math.pi*r*r*r
    print('TSA of sphere',TSA,'volume of sphere',v)
sph(2)

def stdinfo(sid,sname,course,fee=10000):
    print(sname,'is holding id',sid,'and taking course',course,'and paid the fee',fee)

stdinfo(15158,'Danny','python',10000)#we need give the same order given in the def function. 
stdinfo(sname='Danny',sid=15158,course='python',fee=10000)
stdinfo(15158,sname='Danny',course='python',fee=10000)
stdinfo(sname='Danny',sid=15158,course='python')

