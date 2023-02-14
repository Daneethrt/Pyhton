'''#identity operator(is,isnot).
#if A and B are not equal values.
a=25
b=35
print(id(a))
print(id(b))
print(a is b)#false
print(a is not b)#false is changed to true
print(a==b)# false
#----------------------------------------------------------------------------------------------------------------------------

#identity operator(is,isnot).
#if C and D are equal values.
c=25
d=25
print(id(c))
print(id(d))
print(c is d)#true
print(c is not d)#true is changed to false.
print(c==d)# true
#----------------------------------------------------------------------------------------------------------------------------
'''
#Membership operator(in,notin).
l1=[35,60,58,59,70,55,78]
l2=[61,85,98,95,66,78,88]
print(40 in l1 and l2)
print(78 in l2)
print(78 not in l1)
