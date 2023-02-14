#To find avarage.
def stdinfo(sname,m1,m2,m3,m4,m5):
    a=(m1+m2+m3+m4+m5)/5
    print(sname,'has scored the average',a)

stdinfo('Danny',90,85,86,88,85)

def stdinfo(sname,*marks):
    a=sum(marks)/len(marks)
    print(sname,'has scored the average',a)
stdinfo('Danny',90,85,86,88,85)
stdinfo('daneeth',90,65,70,55,58,95,67)


def stdinfo(sid,name,*marks,mobno):
    t=sum(marks)
    print(name,'is holdng',sid,'and moblie number ',mobno,'and scored the total marks in all subjects is',t)


stdinfo(15158,'daneeth',50,60,40,70,80,90,9488230333)
#stdinfo(sid=15158,name='daneeth',t=50,60,40,70,80,90,mobno=9488230333)
#stdinfo(sid=15158,name='daneeth',t=50,t=60,t=40,t=70,t=80,t=90,mobno=9488230333)


