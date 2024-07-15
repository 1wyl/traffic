import initialize
import update
import reorder
times=8
Deltat=0.1
Q=1
set=[]
while Q<=times:
    timeset=[]
    cars=initialize.initialize1()
    initialize.initialize2(cars)
    initialize.initialize3(cars)
    Cars=update.allocate(cars)
    for carlist in Cars:
        update.lightset(carlist,200,0.2,11)
    n=0
    T=0
    while not all(carlist==[] for carlist in Cars):
        n+=1
        T+=Deltat
        print("第",n,"次更新")
        for carlist in Cars:
            speeds=[]
            for car in carlist:
                speeds+=[car.speed]
            [carlist,timeset]=update.inupdate1(carlist,timeset,n,speeds)
        Cars=update.reallocate(Cars)
        for carlist in Cars:
            update.lightset(carlist,5,0.3,20)
            carlist=reorder.reorder(carlist)
            update.update2(carlist) 
    set+=[round(max(timeset),2)]
    print("第",Q,"次智能模拟完成,模拟时间为",max(timeset))
    Q+=1
print("智能模拟的时间集合为:",set,"平均值为",'%.2f' % float(sum(set)/len(set)))
