'''#Get ood numbers using for loop
r=range(61,90,2)
for i in r:
    print(i)

#Get ood numbers using for loop
r=range(60,90)
for i in r:
    if i%2!=0:
        print(i)
'''
#getting stars.

for i in range(1,6):
    for j in range(1,i+1):
        print('*',end='')
    print()
    
#getting stars-2.
for i in range(1,6):
    print(''*i,end='')
    print('*'*i,end='')
    print()
     
