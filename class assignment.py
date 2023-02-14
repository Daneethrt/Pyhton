nn=20
while(nn<=50):
 if(nn%2==0):
  print(nn)
 nn=nn+1

#Take a number and print the sum of number.


n=int(input('enter a number:'))
on=n
r=0
while (n>0):
    r=r+(n%10)
    n=n//10
print('The sum of the digits of',on,'is',r)
 
#reverse the number
num=int(input('Enter a number:'))
remi=0
while(num>0):
    remi=(remi*10)+(num%10)
    num=num//10
print(remi)
 
#To find a number is prme or not.

numb=int(input('Enter a number:'))
i=1
f=0
while(i<=numb):
    if(numb%i==0):
        f=f+1
    i=i+1
print(f)
if(f==2):
    print(numb,'is a prime number')
else:
    print(numb,'is not a prime number')





   
