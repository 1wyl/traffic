import initialize
import update
import reorder
import gc
times=100
Deltat=1
Q=1
set=[]
while Q<=times:
    cars=initialize.initialize1()
    initialize.initialize2(cars)
    initialize.initialize3(cars)
    n=0
    T=0
    timeset=[]
    while True:
        n+=1
        T+=Deltat
        speeds=[]
        for car in cars:
            speeds+=[car.speed]
        [cars,timeset]=update.update1(cars,timeset,n,speeds)
        if cars==[]:
            break
        else:
            cars=reorder.reorder(cars)
            update.update2(cars) 
    cars.clear()
    del cars
    gc.collect()
    Q+=1
    set+=[max(timeset)]
    print("第",Q-1,"次非智能模拟完成,模拟时间为",max(timeset))
print("非智能模拟的时间集合为:",set,"平均值为",'%.2f' % float(sum(set)/len(set)))
