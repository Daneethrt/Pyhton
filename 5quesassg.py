'''#1)Write a program which will find all such numbers which are divisible by 9 but are not a multiple of 4,between 1000 and 2000.
for i in range(1000,2000):
    if(i%9==0 and i%4!=0):
        print(i)'''

#2) Write a program that calculates and prints the value according to the given formula:
#Q = Square root of [(2 * C * D)/H]
#Following are the fixed values of C and H:
#C is 50. H is 30.
#D is the variable whose values should be input to your program in a comma-separated sequence.

'''import math
numbers = input("Provide D: ")
numbers = numbers.split(',')
for D in numbers:
    Q = (math.sqrt(2 * 50 * int(D) / 30))   
print(Q)'''

#3)write a program printing first 30 natural numbers.But print
#i) aaza for all multiples of 2
#ii) baza for all multiples of 3
#iii) caza for all multiples of 5
#iv) aazabaza for all multiples of 2,3 together
#v) aazacaza for all multiples of 2,5  together
#vi) bazacaza for all multiples of 3,5 together
#vii) aazabazacaza for all multiples of 2,3,5 together

def f(n):
    for i in range(1,n+1):
        if (i%2==0):
            print('aaza',i)
        if(i%3==0):
            print('baza',i)
        if(i%5==0):
            print('caza',i)
        if(i%2==0 and i%3==0):
            print('aazabaza',i)
        if(i%2==0 and i%5==0):
            print('aazacaza',i)
        if(i%3==0 and i%5==0):
            print('bazacaza',i)
        if(i%2==0 and i%3==0 and i%5==0):
            print('aazabazacaza',i)       
f(30)            

    
'''#5)Define a function that can accept two strings as input and print the string with maximum length in console. If two strings have the same length, then the function should print al l strings line by line.
def f1(s1, s2):
    if len(s1) > len(s2):
        print('String 1 is longer: ', s1)
    elif len(s1) < len(s2):
        print('String 2 is longer: ', s2)
    else:
        print('Strings length are equal!')

        
f1('Daneeth','Daneeth Reddy')'''
    
    
    

