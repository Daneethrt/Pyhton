import os,sys
name=input('please enter the file name:')
if os.path.isfile(name):
    print('The file',name,'is existing')
    f=open(name,'r')
else:
    print('The file',name,'is not existing')
    sys.exit(0)
data=f.read()
numofchar=len(data)
numofwords=len(data.split())
numoflines=len(data.splitlines())
print(data)
print('Number of characters is:',numofchar)
print('Number of words is:',numofwords)
print('Number of lines is:',numoflines)

