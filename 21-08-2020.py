#To create CSV module(which creates execel file).
'''import csv
f=open('std.csv','w')
w=csv.writer(f)
w.writerow(['SID','NAME','COURSE','FEE','MOBILENO'])
n=int(input('please enter the no of students:'))
for i in range(n):
    sno=int(input('please enter your id:'))
    sname=input('please enter your sname:')
    crs=input('please enter your course:')
    fee=int(input('please enter your fee:'))
    mob=int(input('please enter your mobile no:'))
    w.writerow([sno,sname,crs,fee,mob]) 
f.close()'''


'''f1=open('danny2.txt','w')
f2=open('danny3.txt','w')

f1.close()
f2.close()'''

'''#To create Zip file module(whch create zip file)
from zipfile import*
f=ZipFile('sinpo.zip','w',ZIP_DEFLATED)
f.write('danny.txt')
f.write('danny1.txt')
f.write('danny2.txt')
f.write('danny3.txt')
f.write('std.csv')
f.close()'''

from zipfile import*
f=ZipFile('sinpo.zip','r',ZIP_STORED)
print(f.read())
f.close()


