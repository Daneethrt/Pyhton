'''def stdinfo(sname,m1,m2,m3):
    a=(m1+m2+m3)/3
    print(sname,'has scored the average',a)

stdinfo('danny',58,58,58)

def stdinfo(sid,sname,course,fee):
    print(sname,'is holding id',sid,'and taking course',course,'and paid the fee',fee)

stdinfo(15158,'Danny','python',10000)#we need give the same order given in the def function. 
stdinfo(sname='Danny',sid=15158,course='python',fee=10000)
'''      
def rec(l,b):
    print('Area of rectangle is',l*b,'perimeter of rectangle is',(2*(l+b)))  
rec(1,2)

def rec(l,b):
    print('Area of rectangle is',l*b)
    print( 'perimeter of rectangle is',(2*(l+b)))
rec(1,3)

def d1(a,b):
    if(a>=b):
        print('A has largest value than B, Value is',a)
    else:
        print('B has largest value than A, Value is',b)

     

d1(10,20)
d1(200,100)
