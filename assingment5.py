#To get star in praymid form.
for i in range(1,6):
    print(' '*(5-i),end='')
    for j in range(1,i+1):
        print('*',end='')
    print()

#Method-2 for stars.
for i in range(1,6):
    print(' '*(5-i)+'*'*i)

#method-3 for stars.
for i in range(1,6):
    print(' '*(5-i),end='')
    print('*'*i,end='')
    print()

#Method-4 for stars.
n=int(input('Enter the number:'))
for i in range(1,n+1):
    print(' '*(n-i)+'*'*i)

#Numbers in praymid space.    
for i in range(1,6):
    print(' '*(5-i),end='')
    for j in range(1,i+1):
        print(j,end='')
    print()

#method-2 for numbers.
n=int(input('Enter the number:'))
for i in range(1,n+1):
    print(' '*(n-i),end='')
    for j in range(1,i+1):
        print(j,end='')
    print()
