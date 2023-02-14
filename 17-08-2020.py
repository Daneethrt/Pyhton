# Code for multiple lines for writting.
f=open('danny.txt','w')
f.write('Tadiparthi Daneeth Reddy \n')
f.write('Amrita university  \n')
f.write('Coimbatore \n')
print(f.mode)
print(f.name)
print(f.readable())
print(f.writable())
print(f.closed)
f.close()
print(f.closed)

'''# code of appending(a).
f=open('danny.txt','a')
f.write('Tadiparthi Daneeth Reddy \n')
f.write('Amrita university  \n')
f.write('Coimbatore \n')
print(f.mode)
print(f.name)
print(f.readable())
print(f.writable())
print(f.closed)
f.close()
print(f.closed)'''

'''# code of appending(a) with different name.
f=open('danny1.txt','a')
f.write('Tadiparthi Daneeth Reddy \n')
f.write('Amrita university  \n')
f.write('Coimbatore \n')
print(f.mode)
print(f.name)
print(f.readable())
print(f.writable())
print(f.closed)
f.close()
print(f.closed)'''

f=open('danny.txt','w')
f.write('948823033 \n')
f.write('india \n')
f.write('pin-641112 \n')
f.close()

#code of read mode(r)
f=open('danny.txt','r')
print(f.read())
print(f.read(10))
print(f.readline())
print(f.readlines())
f.close()

