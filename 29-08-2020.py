'''import array
a=array.array('i',[76,86,88,77])
print(a.pop())
print(a[:])
a.remove(81)
print(a)
#for i in range(4):
    #print(a[i])'''

'''import numpy as np
a=np.array([[3,4],[6,7]])
b=np.array([[30,40],[15,17]])
print('addition a and b matrix is',a+b)
print('subtraction a and b matrix is',a-b)
r=np.add(a,b)
print('addition a and b matrix is',r)
r=np.dot(a,b)
print('Multiple of a and b matrix is',r)'''


import numpy as np
Q=np.array([[2,-2,-4],[-1,3,4],[1,-2,-3]])
a=np.dot(Q,Q)
if(Q==a):
    print('The given is ideompotent matrix',a)
else:
    print('The given is not ideompotent matrix',a)

