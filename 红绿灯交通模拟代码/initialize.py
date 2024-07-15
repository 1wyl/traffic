import random
pi=3.14
eachnumber=60
class Car:
    def __init__(self,direction,coordinate):
        self.direction=direction
        self.coordinate = coordinate
        self.serial=0
        self.disstopline = 0
        self.dislimitation=0
        self.light = 1
        self.lis = []
        self.speed = 17
        self.d_c = 50
        self.acceleration=0
        self.d_v=0
        self.time=0
        self.intersection=0
def makedisstopline(self,n):
    self.disstopline=(n-1)*50+1200
def listmaker(p1, p2):
    p = [0, 0]
    p[0] = p2[0] - p1[0]
    p[1] = p2[1] - p1[1]
    if p1[1] == -2:
        pass
    elif p1[1] == 2:
        p[0] = -p[0]
        p[1] = -p[1]
    elif p1[0] == 2:
        t = p[0]
        p[0] = p[1]
        p[1] = -t
    elif p1[0] == -2:
        t = p[0]
        p[0] = -p[1]
        p[1] = t
    if p[1] == 4:  # 由底到顶
        if p[0] == 0:
            return [0, 0, 0]  
        elif p[0] == -1:
            return [-1, 1, 0, 0]
        elif p[0] == -2:
            return [-1, 0, 1, 0, 0]
        elif p[0] == 1:
            return [1, -1, 0, 0]
        elif p[0] == 2:
            return [1, 0, -1, 0, 0]
    elif p[1] == 0:  # 由底到底
        if p[0] == -1:
            return [-1, -1]
        elif p[0] == 1:
            return [1, 1]
        elif p[0] == -2:
            return [-1, 0, -1]
        elif p[0] == 2:
            return [1, 0, 1]
    else:  # 由底到边
        temporary = []
        if p[1] > 1:
            for i in range(p[1] - 1):
                temporary += [0]  
            if p[0] > 0:
                temporary += [1]  
                for j in range(p[0] - 1):
                    temporary += [0]  
                return temporary
            elif p[0] < 0:
                temporary += [-1]  
                for j in range(p[0] - 1):
                    temporary += [0] 
                return temporary
        else:  
            if p[0] > 0:
                temporary += [1]  
                for j in range(p[0] - 1):
                    temporary += [0]  
                return temporary
            elif p[0] < 0:
                temporary += [-1]  
                for j in range(p[0] - 1):
                    temporary += [0]  
                return temporary
def makelis(self):
    positions = [[-1, -2], [-1, 2], [0, -2], [0, 2], [1, -2], [1, 2], [-2, -1], [2, -1], [-2, 0], [2, 0], [-2, 1],[2, 1]]
    positions.remove(self.coordinate)
    outposition = random.choice(positions)
    self.lis = listmaker(self.coordinate, outposition)
def makeserial(self):
    if self.lis[0]==-1:
        self.serial=-1
    elif self.lis[0] ==1:
        self.serial=1
    else:
        self.serial = 0
def makelight(self):
    if self.serial==1:
        self.light=1
    else:
        if self.direction==[0,1]:
            self.light=1
        else:
            self.light=-1
def makedislimitation(self):
    if self.serial == -1:
        self.dislimitation=14*pi
    elif self.serial == 1:
        self.dislimitation=2*pi
    else:
        self.dislimitation =48
def initialize2(cars):
    for car in cars:
        makelis(car)
        makeserial(car)
        makelight(car)
        makedislimitation(car)
def initialize1():
    directions=[[1,0],[-1,0],[0,1],[0,-1]]
    coordinates = [[-2, -1], [-2, 0], [-2, 1]], [[2, -1], [2, 0], [2, 1]], [[-1, -2], [0, -2], [1, -2]], [[-1, 2], [0, 2], [1, 2]]
    cars=[]
    i=0
    for direction in directions:
        for coordinate in coordinates[i]:
            for j in range(eachnumber):
                cars+=[Car(direction,coordinate)]
        i+=1
    return cars
def initialize3(cars):
    zushu=int(len(cars)/eachnumber)
    for i in range(zushu):
        serialminus = 0
        serialzero = 0
        serialplus = 0
        for j in range(eachnumber):
            if cars[i * eachnumber + j].serial==-1:
                serialminus+=1
                makedisstopline(cars[i*eachnumber+j],serialminus)
            elif cars[i * eachnumber + j].serial == 0:
                serialzero+=1
                makedisstopline(cars[i * eachnumber + j], serialzero)
            elif cars[i * eachnumber + j].serial == 1:
                serialplus+=1
                makedisstopline(cars[i * eachnumber + j], serialplus)