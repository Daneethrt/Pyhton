# recurisve functon.
def fctr(n):
    if(n==1 or n==0):
        return 1
    else:
         return n*fctr(n-1)
        
   
x=fctr(3)
print(x)
'''
#adding natural numbers.
def nat(n):
    f=0
    for i in range(1,n+1):
        f=f+i
    return f

    
x=nat(10)
print(x)
'''
