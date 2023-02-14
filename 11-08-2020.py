#Fibonacci series in recursion
#fn=fn-1+fn-2
def n1(n):
    if n<=1:
        return n
    else:
        return(n1(n-1)+n1(n-2))

x=n1(2)
print(x)
