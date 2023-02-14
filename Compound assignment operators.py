'''#assignment operators and compound assignment(+=,-=,*=,/=,//=,**=,%=)
#// gives value before decimal ex:10/4=2.5, for // it gives ans as 2
#% gives value after decimal ex:10/4=2.5, for % it gives ans as 2

#code for +=
a=25
b=3
a+=10#which gives 25+10=35
b+=4#which gives 4+3=7
print(a)
print(b)
print(a+b)#addition,which gives 35+7=42
print(a-b)#subtraction,which gives 35-7=28
print(a*b)#multplication,which gives 35*7=245
print(a/b)#division,which gives 35/7=5.0
print(a%b)#modulo,which gives 35%7=0
print(a//b)#floor division,which gives 35//7=5
print(a**b)#exponent,whch gives35^7=64339296875
print(a<b)#lesser, which give Flase(35<7)
print(a>b)#greater, which give True(35>7)
print(a<=b)#lesser than equal to, which give False(35<=7)
print(a>=b)#greater than equal to, which give True(35>=7)
print(a==b)#equal to, which give flase(35==7)
print(a!=b)#not equal to, which give True(35!=7)
#-------------------------------------------------------------------------------
#code for -=
c=25
d=10
c-=10
d-=3
print(c)
print(d)
print(c+d)#addition,which gives 15+7=22
print(c-d)#subtraction,which gives 15-7=8
print(c*d)#multplication,which gives 15*7=105
print(c/d)#division,which gives 15/7=2.14
print(c%d)#modulo,which gives 15%7=1
print(c//d)#floor division,which gives 15//7=2
print(c**d)#exponent,whch gives15^7=1708593375
print(c<d)#lesser, which give Flase(15<7)
print(c>d)#greater, which give True(15>7)
print(c<=d)#lesser than equal to, which give False(15<=7)
print(c>=d)#greater than equal to, which give True(15>=7)
print(c==d)#equal to, which give flase(15==7)
print(c!=d)#not equal to, which give True(15!=7)
#-------------------------------------------------------------------------------
#code for *=
e=5
f=2
e*=3
f*=5
print(e)#ouput is 5*3=15
print(f)#output is 2*5=10
print(e+f)#add, which gives 15+10=25
print(e-f)#sub, which gives 15-10=5
print(e*f)#mup, which gives 15*10=150
print(e/f)#div, which gives 15/10=1.5
print(e%f)#modulo, which gives 15%10=5
print(e//f)#floor div, which gives 15//10=1
print(e**f)#exponent, which gives 15^10=576650390625
print(e<f)#lesser, which gives Flase,(15<7)
print(e>f)#greater, which gives True,(15>7)
print(e<=f)#lesser than equal to, which gives Flase,(15<=7)
print(e>=f)#greater than equal to, which gives True,(15>=7)
print(e==f)#equal to, which gives Flase,(15==7)
print(e!=f)#not equal to, which gives True,(15!=7)
#-------------------------------------------------------------------------------
#code for /=
e=10
f=20
e/=2
f/=2
print(e)#ouput is 10/2=5
print(f)#output is 20/2=10
print(e+f)#add, which gives 5+10=15
print(e-f)#sub, which gives 5-10=-5
print(e*f)#mup, which gives 5*10=50
print(e/f)#div, which gives 5/10=0.5
print(e%f)#modulo, which gives 5%10=5
print(e//f)#floor div, which gives 5//10=0
print(e**f)#exponent, which gives 5^10=9765625
print(e<f)#lesser, which gives True,(5<10)
print(e>f)#greater, which gives Flase,(5>10)
print(e<=f)#lesser than equal to, which gives True,(5<=10)
print(e>=f)#greater than equal to, which gives Flase,(5>=10)
print(e==f)#equal to, which gives Flase,(15==7)
print(e!=f)#not equal to, which gives True,(15!=7)
#-------------------------------------------------------------------------------
#code for //=
e=10
f=20
e//=5
f//=5
print(e)#ouput is 10//5=2
print(f)#output is 20//5=4
print(e+f)#add, which gives 2+4=6
print(e-f)#sub, which gives 2-4=-2
print(e*f)#mup, which gives 2*4=8
print(e/f)#div, which gives 2/4=0.5
print(e%f)#modulo, which gives 2%4=2
print(e//f)#floor div, which gives 2//4=0
print(e**f)#exponent, which gives 2^4=16
print(e<f)#lesser, which gives True,(2<4)
print(e>f)#greater, which gives Flase,(2>4)
print(e<=f)#lesser than equal to, which gives True,(2<=4)
print(e>=f)#greater than equal to, which gives Flase,(2>=4)
print(e==f)#equal to, which gives Flase,(2==4)
print(e!=f)#not equal to, which gives True,(2!=4)
#-------------------------------------------------------------------------------
#code for %=
e=10
f=20
e//=4
f//=8
print(e)#ouput is 10%5=2
print(f)#output is 20%5=2
print(e+f)#add, which gives 2+2=4
print(e-f)#sub, which gives 2-2=0
print(e*f)#mup, which gives 2*2=4.0
print(e/f)#div, which gives 2/2=1
print(e%f)#modulo, which gives 2%2=0
print(e//f)#floor div, which gives 2//2=1
print(e**f)#exponent, which gives 2^2=4
print(e<f)#lesser, which gives Flase,(2<2)
print(e>f)#greater, which gives Flase,(2>2)
print(e<=f)#lesser than equal to, which gives True,(2<=2)
print(e>=f)#greater than equal to, which gives True,(2>=2)
print(e==f)#equal to, which gives True,(2==2)
print(e!=f)#not equal to, which gives Flase,(2!=2)'''
#-------------------------------------------------------------------------------
#code for **=
e=2
f=2
e**=3
f**=2
print(e)#ouput is 2**3=8
print(f)#output is 2**2=4
print(e+f)#add, which gives 8+4=12
print(e-f)#sub, which gives 8-4=4
print(e*f)#mup, which gives 8*4=32
print(e/f)#div, which gives 8/4=2.0
print(e%f)#modulo, which gives 8%4=0
print(e//f)#floor div, which gives 8//4=2
print(e**f)#exponent, which gives 8^4=4096
print(e<f)#lesser, which gives Flase,(8<4)
print(e>f)#greater, which gives True,(8>4)
print(e<=f)#lesser than equal to, which gives Flase,(8<=4)
print(e>=f)#greater than equal to, which gives True,(8>=4)
print(e==f)#equal to, which gives Flase,(8==4)
print(e!=f)#not equal to, which gives True,(8!=4)


