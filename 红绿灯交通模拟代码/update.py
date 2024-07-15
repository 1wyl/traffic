import math
pi=3.14
Deltat=1
def lasttime(s,v):#以初速度v，加速度为a，限速17m/s,行驶最后s所用时间的计算公式 
    a=2
    if s<=(17**2-v**2)/2/a:
        if v**2+2*a*s>=0:
            t=-v/a+math.sqrt(v**2+2*a*s)/a
        else:
            t=-v/a
    else:
        t=s/17-(17**2-v**2)/34/a
    return t
def lightchange(self,T):
    if self.direction==[0,1]:
        if T%120>=0 and T%120<=27:
            self.light=1
        elif T%120>27 and T%120<=30:
            self.light=0
        elif T%120>30 and T%120<120:
            self.light=-1
    elif self.direction==[-1,0]:
        if (T-30)%120>=0 and (T-30)%120<=27:
            self.light=1
        elif (T-30)%120>27 and (T-30)%120<=30:
            self.light=0
        elif (T-30)%120>30 and (T-30)%120<120:
            self.light=-1
    elif self.direction==[0,-1]:
        if (T-60)%120>=0 and (T-60)%120<=27:
            self.light=1
        elif (T-60)%120>27 and (T-60)%120<=30:
            self.light=0
        elif (T-60)%120>30 and (T-60)%120<120:
            self.light=-1
    elif self.direction==[1,0]:
        if (T-90)%120>=0 and (T-90)%120<=27:
            self.light=1
        elif (T-90)%120>27 and (T-90)%120<=30:
            self.light=0
        elif (T-90)%120>30 and (T-90)%120<120:
            self.light=-1
def lightchange2(self,T,t):
    T2=4*(t+3)
    if self.direction==[0,1]:
        if T%T2>=0 and T%T2<=t:
            self.light=1
        elif T%T2>t and T%T2<=t+3:
            self.light=0
        elif T%T2>t+3 and T%T2<T2:
            self.light=-1
    elif self.direction==[-1,0]:
        if (T-t-3)%T2>=0 and (T-t-3)%T2<=t:
            self.light=1
        elif (T-t-3)%T2>t and (T-t-3)%T2<=t+3:
            self.light=0
        elif (T-t-3)%T2>t+3 and (T-t-3)%T2<T2:
            self.light=-1
    elif self.direction==[0,-1]:
        if (T-2*t-6)%T2>=0 and (T-2*t-6)%T2<=t:
            self.light=1
        elif (T-2*t-6)%T2>t and (T-2*t-6)%T2<=t+3:
            self.light=0
        elif (T-2*t-6)%T2>t+3 and (T-2*t-6)%T2<T2:
            self.light=-1
    elif self.direction==[1,0]:
        if (T-3*t-9)%T2>=0 and (T-3*t-9)%T2<=t:
            self.light=1
        elif (T-3*t-9)%T2>t and (T-3*t-9)%T2<=t+3:
            self.light=0
        elif (T-3*t-9)%T2>t+3 and (T-3*t-9)%T2<T2:
            self.light=-1
def update1s(cars,timeset,n,speeds,w):
    T=n*Deltat
    records=[]
    L=len(cars)
    for i in range(L):
        cars[i].disstopline = cars[i].disstopline - speeds[i] * Deltat
        cars[i].speed = cars[i].speed + cars[i].acceleration * Deltat
        if cars[i].disstopline>0:
            if cars[i].serial != 1:
                lightchange2(cars[i],T,w)
        else:
            if cars[i].lis==[]:
                cars[i].lis+=[0]
            cars[i].lis.pop(0)
            if cars[i].lis==[]:
                timeset +=[T+lasttime(1200+cars[i].dislimitation+cars[i].disstopline,cars[i].speed)]
                records+=[i]
            else:
                updatecoordinate(cars[i])
                directionchange(cars[i])
                cars[i].serial=cars[i].lis[0]
                cars[i].disstopline = 1200+cars[i].dislimitation+cars[i].disstopline
                makedislimitation(cars[i])
                if cars[i].serial != 1:
                    lightchange2(cars[i],T,w)
                else:
                    cars[i].light=1
    records.reverse()
    for record in records:
        cars.pop(record)
    cars=revise(cars)
    return [cars,timeset]
def directionchange(self):
    if self.serial==1:
        temp=self.direction[0]
        self.direction[0]=self.direction[1]
        self.direction[1]=-temp
    elif self.serial==-1:
        temp = self.direction[0]
        self.direction[0] = -self.direction[1]
        self.direction[1] = temp
def updatecoordinate(self):
    if self.direction == [1,0] and self.serial==-1:#右上
        if self.coordinate[0]<=-1:
            self.coordinate[0]+=1
        if self.coordinate[1]>=0:
            self.coordinate[1]+=1
    elif self.direction == [-1,0] and self.serial==1:#左上
        if self.coordinate[0]>=1:
            self.coordinate[0]-=1
        if self.coordinate[1]>=0:
            self.coordinate[1]+=1
    elif self.direction == [1,0] and self.serial==1:#右下
        if self.coordinate[0]<=-1:
            self.coordinate[0]+=1
        if self.coordinate[1]<=0:
            self.coordinate[1]-=1
    elif self.direction == [-1,0] and self.serial==-1:#左下
        if self.coordinate[0]>=1:
            self.coordinate[0]-=1
        if self.coordinate[1]<=0:
            self.coordinate[1]-=1
    elif self.direction == [0,1] and self.serial==-1:#上左
        if self.coordinate[1]<=-1:
            self.coordinate[1]+=1
        if self.coordinate[0]<=0:
            self.coordinate[0]-=1
    elif self.direction == [0,-1] and self.serial==1:#下左
        if self.coordinate[1]>=1:
            self.coordinate[1]-=1
        if self.coordinate[0]<=0:
            self.coordinate[0]-=1
    elif self.direction == [0,1] and self.serial==1:#上右
        if self.coordinate[1]<=-1:
            self.coordinate[1]+=1
        if self.coordinate[0]>=0:
            self.coordinate[0]+=1
    elif self.direction == [0,-1] and self.serial==-1:#下右
        if self.coordinate[1]>=1:
            self.coordinate[1]-=1
        if self.coordinate[0]>=0:
            self.coordinate[0]+=1
def makedislimitation(self):
    if self.serial == -1:
        self.dislimitation=14*pi
    elif self.serial == 1:
        self.dislimitation=2*pi
    else:
        self.dislimitation =48
def revise(cars):
    for car in cars:
        if car.lis==[]:
            cars.remove(car)
    for car in cars:
        if car.speed>17:
            car.speed=17
        elif car.speed<0:
            car.speed=0
    return cars
def update1(cars,timeset,n,speeds):
    T=n*Deltat
    records=[]
    L=len(cars)
    for i in range(L):
        cars[i].disstopline = cars[i].disstopline - speeds[i] * Deltat
        cars[i].speed = cars[i].speed + cars[i].acceleration * Deltat
        if cars[i].disstopline>0:
            if cars[i].serial != 1:
                lightchange(cars[i],T)
        else:
            if cars[i].lis==[]:
                cars[i].lis+=[0]
            cars[i].lis.pop(0)
            if cars[i].lis==[]:
                timeset +=[T+lasttime(1200+cars[i].dislimitation+cars[i].disstopline,cars[i].speed)]
                records+=[i]
            else:
                updatecoordinate(cars[i])
                directionchange(cars[i])
                cars[i].serial=cars[i].lis[0]
                cars[i].disstopline = 1200+cars[i].dislimitation+cars[i].disstopline
                makedislimitation(cars[i])
                if cars[i].serial != 1:
                    lightchange(cars[i],T)
                else:
                    cars[i].light=1
    records.reverse()
    for record in records:
        cars.pop(record)
    cars=revise(cars)
    return [cars,timeset]
def updateacc1(self):
    if self.disstopline>100:
        if 17-self.speed<2*Deltat:
            self.acceleration=(17-self.speed)/Deltat
        else:
            self.acceleration=2
    elif self.disstopline>=20 and self.disstopline<=100:
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
                a=-2
def updateacc2(self):
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
def update2(cars):
    i=0
    for car in cars:
        i+=1
        if car.d_v==None:
            updateacc1(car)
        else:
            updateacc2(car)
            
def judge0(car):
    if (car.direction==[1,0] and car.coordinate==[-2,1]) or (car.direction==[-1,0] and car.coordinate==[-1,1]) or (car.direction==[0,-1] and car.coordinate==[-1,2]) or (car.direction==[0,1] and car.coordinate==[-1,1]):
        return True
def judge1(car):
    if (car.direction==[1,0] and car.coordinate==[-1,1]) or (car.direction==[-1,0] and car.coordinate==[1,1]) or (car.direction==[0,-1] and car.coordinate==[0,2]) or (car.direction==[0,1] and car.coordinate==[0,1]):
        return True
def judge2(car):
    if (car.direction==[1,0] and car.coordinate==[1,1]) or (car.direction==[-1,0] and car.coordinate==[2,1]) or (car.direction==[0,-1] and car.coordinate==[1,2]) or (car.direction==[0,1] and car.coordinate==[1,1]):
        return True
def judge3(car):
    if (car.direction==[1,0] and car.coordinate==[-2,0]) or (car.direction==[-1,0] and car.coordinate==[-1,0]) or (car.direction==[0,-1] and car.coordinate==[-1,1]) or (car.direction==[0,1] and car.coordinate==[-1,-1]):
        return True
def judge4(car):
    if (car.direction==[1,0] and car.coordinate==[-1,0]) or (car.direction==[-1,0] and car.coordinate==[1,0]) or (car.direction==[0,-1] and car.coordinate==[0,1]) or (car.direction==[0,1] and car.coordinate==[0,-1]):
        return True
def judge5(car):
    if (car.direction==[1,0] and car.coordinate==[1,0]) or (car.direction==[-1,0] and car.coordinate==[2,0]) or (car.direction==[0,-1] and car.coordinate==[1,1]) or (car.direction==[0,1] and car.coordinate==[1,-1]):
        return True
def judge6(car):
    if (car.direction==[1,0] and car.coordinate==[-2,-1]) or (car.direction==[-1,0] and car.coordinate==[-1,-1]) or (car.direction==[0,-1] and car.coordinate==[-1,-1]) or (car.direction==[0,1] and car.coordinate==[-1,-2]):
        return True
def judge7(car):
    if (car.direction==[1,0] and car.coordinate==[-1,-1]) or (car.direction==[-1,0] and car.coordinate==[1,-1]) or (car.direction==[0,-1] and car.coordinate==[0,-1]) or (car.direction==[0,1] and car.coordinate==[0,-2]):
        return True
def judge8(car):
    if (car.direction==[1,0] and car.coordinate==[1,-1]) or (car.direction==[-1,0] and car.coordinate==[2,-1]) or (car.direction==[0,-1] and car.coordinate==[1,-1]) or (car.direction==[0,1] and car.coordinate==[1,-2]):
        return True
def allocate(cars):
    Cars=[]
    for i in range(9):
        Cars+=[[]]
    for car in cars:
        if judge0(car):
            car.intersection=0
            Cars[0]+=[car]
        elif judge1(car):
            car.intersection=1
            Cars[1]+=[car]
        elif judge2(car):
            car.intersection=2
            Cars[2]+=[car]
        elif judge3(car):
            car.intersection=3
            Cars[3]+=[car]
        elif judge4(car):
            car.intersection=4
            Cars[4]+=[car]
        elif judge5(car):
            car.intersection=5
            Cars[5]+=[car]
        elif judge6(car):
            car.intersection=6
            Cars[6]+=[car]
        elif judge7(car):
            car.intersection=7
            Cars[7]+=[car]
        elif judge8(car):
            car.intersection=8
            Cars[8]+=[car]
    return Cars
def renewintersection(car):
    if judge0(car):
        car.intersection=0
    elif judge1(car):
        car.intersection=1
    elif judge2(car):
        car.intersection=2
    elif judge3(car):
        car.intersection=3
    elif judge4(car):
        car.intersection=4
    elif judge5(car):
        car.intersection=5
    elif judge6(car):
        car.intersection=6
    elif judge7(car):
        car.intersection=7
    elif judge8(car):
        car.intersection=8
def inupdate1(cars,timeset,n,speeds):
    T=n*Deltat
    records=[]
    L=len(cars)
    for i in range(L):
        cars[i].time-=Deltat
        cars[i].disstopline = cars[i].disstopline - speeds[i] * Deltat
        cars[i].speed = cars[i].speed + cars[i].acceleration * Deltat
        if cars[i].disstopline>0:
            pass
        else:
            if cars[i].lis==[]:
                cars[i].lis+=[0]
            cars[i].lis.pop(0)
            if cars[i].lis==[]:
                timeset +=[T+lasttime(1200+cars[i].dislimitation+cars[i].disstopline,cars[i].speed)]
                records+=[i]
            else:
                updatecoordinate(cars[i])
                directionchange(cars[i])
                renewintersection(cars[i])
                cars[i].serial=cars[i].lis[0]
                cars[i].disstopline = 1200+cars[i].dislimitation+cars[i].disstopline
                makedislimitation(cars[i])
    records.reverse()
    for record in records:
        cars.pop(record)
    revise(cars)
    return [cars,timeset]
def reallocate(Cars):
    for carlist in Cars:
        for car in carlist:
            if car.intersection!=Cars.index(carlist):
                Cars[car.intersection]+=[car]
                carlist.remove(car)
    return Cars
def pri(cars):
    i=0
    for car in cars:
        print("第",i+1,"辆车信息为")
        print("self.lis =", cars[i].lis,
            "self.speed=", cars[i].speed,
            "self.acceleration=", cars[i].acceleration,
            "self.disstopline =", cars[i].disstopline,
            "self.intersection =", cars[i].intersection,
            "self.dislimitation=", cars[i].dislimitation,
            "self.d_v=", cars[i].d_v,
            "self.d_c =", cars[i].d_c,
            "self.direction=", cars[i].direction,
            "self.coordinate =", cars[i].coordinate,
            "self.serial=", cars[i].serial,
            "self.light =", cars[i].light,
            "self.time =", cars[i].time
            )
        i+=1
def lightset(carlist,w1,w2,w3):
    if carlist!=[]:
        if carlist[0].time>=Deltat:
            pass
        else:
            numset=[0,0,0,0]
            disstoplines=[0,0,0,0]
            averds=[0,0,0,0]
            for car in carlist:
                if car.serial!=1 and car.direction==[1,0] and car.disstopline<=w1:
                    numset[0]+=1
                    disstoplines[0]+=car.disstopline
                elif car.serial!=1 and car.direction==[-1,0] and car.disstopline<=w1:
                    numset[1]+=1
                    disstoplines[1]+=car.disstopline
                elif car.serial!=1 and car.direction==[0,-1] and car.disstopline<=w1:
                    numset[2]+=1
                    disstoplines[2]+=car.disstopline
                elif car.serial!=1 and car.direction==[0,1] and car.disstopline<=w1:
                    numset[3]+=1
                    disstoplines[3]+=car.disstopline
            for i in range(4):
                if numset[i]!=0:
                    averds[i]=disstoplines[i]/numset[i]
                else:
                    averds[i]=10000000
            grades=[0,0,0,0]
            for i in range(4):
                grades[i]=numset[i]-w2*averds[i]
            mgindex=grades.index(max(grades))
            if mgindex==0:
                for car in carlist:
                    if car.direction==[1,0]:
                        car.light=1
                    elif car.serial==1:
                        car.light=1
                    else:
                        car.light=-1
            elif mgindex==1:
                for car in carlist:
                    if car.direction==[-1,0]:
                        car.light=1
                    elif car.serial==1:
                        car.light=1
                    else:
                        car.light=-1
            elif mgindex==2:
                for car in carlist:
                    if car.direction==[0,-1]:
                        car.light=1
                    elif car.serial==1:
                        car.light=1
                    else:
                        car.light=-1
            elif mgindex==3:
                for car in carlist:
                    if car.direction==[0,1]:
                        car.light=1
                    elif car.serial==1:
                        car.light=1
                    else:
                        car.light=-1
            for car in carlist:
                car.time=w3
        
        
