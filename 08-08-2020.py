'''#retrun code for addition.
def adds(a,b):
    return(a+b)
x=adds(55,77)
print(x)
x=adds(55,70)
print(x)

#code for rectangle using return.
def rect(l,b):
    area=l*b
    perimeter=2*(l+b)
    return(area,perimeter)
x=rect(20,18)
print('The area of rectangle',x[0],'The perimeter of rectangle',x[1])'''
    
# Find factorial of an number using return function.
def n1(n):
    if(n>=0):
        f=1
        for i in range(n,1,1):
            print(i)
        return f
   
        
x=n1(4)
print(x)
'''
#Print max of three and return min of three.
def maxi(a,b,c):
    if (a>=b) and (a>=c):
        print('A is largest, whos value is:',a)
    elif (b>=a) and (b>=c):
        print('B is largest, whos value is:',b)
    else:
        print('c is largest, which value is:',c)
    return min(a,b,c)
    
x=maxi(10,9,4)
print('The minimum value of x is:',x)
'''
