import initialize
import update
import reorder
import gc
def updateacc1s(self):
    if self.disstopline>85:
        if 17-self.speed<2*Deltat:
            self.acceleration=(17-self.speed)/Deltat
        else:
            self.acceleration=2
    elif self.disstopline>=20 and self.disstopline<=85:
        if self.speed>6:
            if self.speed-6>=2*Deltat:
                self.acceleration=-2
            else:
                self.acceleration=-(self.speed-6)/Deltat
        elif self.speed<6:
            if 6-self.speed>=2*Deltat:
                self.acceleration=2
            else:
                self.acceleration=(6-self.speed)/Deltat
        else:
            self.acceleration=0
    else:
        if self.light==1:
            if abs(self.speed-6)/Deltat<=2:
                self.acceleration=(6-self.speed)/Deltat
            else:
                if self.speed>6:
                    self.acceleration=-2
                else:
                    self.acceleration=2
        else:
            if self.speed/Deltat<=2:
                self.acceleration=-self.speed/Deltat
            else:
                self.acceleration=-2
def updateacc2s(self):
    if self.d_c>3*self.speed and self.d_v<0:
        if -self.d_v>=2*Deltat:
            self.acceleration=2
        else:
            self.acceleration=-self.d_v/Deltat
    elif self.d_c<3*self.speed and self.d_v>0:
        if self.d_v>=2*Deltat:
            self.acceleration=-2
        else:
            self.acceleration=-self.d_v/Deltat
    else:
        self.acceleration=0
def update2s(cars):
    i=0
    for car in cars:
        i+=1
        if car.d_v==None:
            updateacc1s(car)
        else:
            updateacc2s(car)
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
        [cars,timeset]=update.update1s(cars,timeset,n,speeds,11)
        if cars==[]:
            break
        else:
            cars=reorder.reorder(cars)
            update2s(cars) 
    cars.clear()
    del cars
    gc.collect()
    Q+=1
    set+=[max(timeset)]
    print("第",Q-1,"次模拟完成,模拟时间为",max(timeset))
print("模拟的时间集合为:",set,"平均值为",'%.2f' % float(sum(set)/len(set)))