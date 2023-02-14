'''#code for(str,list,tuple,bytes,bytearray,range,set,frozenset,dict)
#code for str
Name='danny'
print(Name)
print('The address of Name',id(Name))#To know address
print('The type of Name',type(Name))#To know type
print(Name[1])#it names with index from 0 to the eixting bits.
print(Name[-3])
#--------------------------------------------------------------------------------------------------------
#code for str2(immutable)
a="Tadiparthi Daneeth Reddy"
print(a)
print(a[0])#output is 'T'
print(a[10])#output is 'space'
print(a[-10])#output is "e"
print(a[-20])#ouput is 'p'
print(a[:])#ouput will be full string
print(a[0:23])#output will be starting from T to d.
print(a[10:])#ouput will be from  Daneeth Reddy.
print(a[:10])#output is Tadiparthi .
print(a[1:9:3])#1+2=3letter,3+2=5values,5+2=7values
print(a[::-1])#ouput is reversed.
print('The address of a',id(a))
print('The address of a',type(a))
#--------------------------------------------------------------------------------------------------------
#list cod(mutable)
#fuction is list()

marks=[58,85,59,95,68,86,66,58]
print('The address of marks',id(marks))
print('The type of marks',type(marks))
marks[6]=77#list is mutable, where we can change the values in the list.
print(marks)
marks.append(66)#it will add the 66number at the end of list.
print(marks)
print(marks.sort())#if strings are there in the list this will not support.
marks.reverse#list is changed from small to big
print(marks)
marks.insert(5,55)#can be inserted any number in list
print(marks)
print(len(marks))#gives the length of list
#--------------------------------------------------------------------------------------------------------
#code for tuple(immutable)
#fuction is tuple()

Marks=(70,94,55,66,77,66,58,85,59)
print('The address of Marks',id(Marks))
print('The type of Marks',type(Marks))
print(Marks)
#--------------------------------------------------------------------------------------------------------
#code for set(mutable)
#fuction is set()

MARKS={70,94,55,66,77,66,58,85,59}#OUPUT willnot be coming in as the same for set like tuple and list.
print('The address of MARKS',id(MARKS))
print('The type of MARKS',type(MARKS))
print(MARKS)
#s[1]=61 will be error there wont be replacement due the change of places of numbers.
MARKS.add(62)
print(MARKS)
#--------------------------------------------------------------------------------------------------------
#frozen set(immutable)
#fuction is frozenset()

fs=frozenset(MARKS)
print('The address of fs',id(fs))
print('The type of fs',type(fs))
#--------------------------------------------------------------------------------------------------------
#code for dict(mutable)
#dict{}

cls={1:'danny',2:'sam',3:'daneeth',4:'jaysam',3:'TDR'}
print(cls)
print(type(cls))
print(cls.keys())
print(cls.values())
cls[2]='sampath'
print(cls)
#--------------------------------------------------------------------------------------------------------
#code for byte(immutable)
#byte() function
#values can be given from 0 to 255 only in the sequence.

b=bytes(MARKS)
print('The address of b',id(b))
print('The type of b',type(b))
#--------------------------------------------------------------------------------------------------------
#code for bytearray(immutable)
#bytearray() function
#values can be given from 0 to 255 only in the sequence.


c=bytearray(MARKS)
print('The address of c',id(c))
print('The type of c',type(c))'''
#--------------------------------------------------------------------------------------------------------
#code for range(immutable) for one arrgument
#range() function

d=range(11)
print(d)
print('The address of d',id(d))
print('The type of d',type(d))
for i in d:
    print(i)
#--------------------------------------------------------------------------------------------------------
#code for range(immutable) for two arrgument
#range() function

e=range(0,11)
print(e)
print('The address of e',id(e))
print('The type of e',type(e))
for i in e:
    print(i)
#--------------------------------------------------------------------------------------------------------
#code for range(immutable) for one arrgument
#range() function

f=range(1,101,2)
print(f)
print('The address of f',id(f))
print('The type of f',type(f))
for i in f:
    print(i)
    
        



