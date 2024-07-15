import initialize
import update
import reorder
import copy
times=2
lastingtimes=[i for i in range(10,35,1)]
set=[0*i for i in range(10,35,1)]
r=1
while r<=times:
    cars=initialize.initialize1()
    initialize.initialize2(cars)
    initialize.initialize3(cars)
    cars2=copy.deepcopy(cars)
    id=0
    for time in lastingtimes:
        Deltat=1
        cars=copy.deepcopy(cars2)
        T=0
        n=0
        timeset=[]
        while True:
            print("第",r,"次初始化","绿灯时长为",time,"的第",n+1,"次更新")
            n+=1
            T+=Deltat
            speeds=[]
            for car in cars:
                speeds+=[car.speed]
            [cars,timeset]=update.update1s(cars,timeset,n,speeds,time)
            if cars==[]:
                break
            else:
                cars=reorder.reorder(cars)
                update.update2(cars) 
        set[id]+=max(timeset)
        id+=1
    r+=1
averset=[set[i]/times for i in range(len(set))]
print(averset)

