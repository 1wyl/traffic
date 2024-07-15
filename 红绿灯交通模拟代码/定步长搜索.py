import initialize
import update
import reorder
import copy
import gc
times=2
Deltat=1
k1=[a for a in range(10,510,10)]
#因变量列表存放[f(a)]
sumdepent=[]
averdepent=[]
p=1
while p<=times:
    cars=initialize.initialize1()
    initialize.initialize2(cars)
    initialize.initialize3(cars)
    Cars0=update.allocate(cars)
    k=1
    for a in k1:
        Cars=copy.deepcopy(Cars0)
        timeset=[]
        for carlist in Cars:
            update.lightset(carlist,a,0,27)
        n=0
        T=0
        while not all(carlist==[] for carlist in Cars):
            n+=1
            T+=Deltat
            for carlist in Cars:
                speeds=[]
                for car in carlist:
                    speeds+=[car.speed]
                [carlist,timeset]=update.inupdate1(carlist,timeset,n,speeds)
            Cars=update.reallocate(Cars)
            for carlist in Cars:
                update.lightset(carlist,a,0,27)
                carlist=reorder.reorder(carlist)
                update.update2(carlist) 
        del Cars
        gc.collect()
        sumdepent+=[max(timeset)]
        print("第",p,"次模拟的","第",k,"次搜索结果记录：",a,max(timeset))
        k+=1
    p+=1
averdepent=[i/times for i in sumdepent]
print("搜索完成")
print("自变量集合\n",k1)
print("因变量集合\n",averdepent)
