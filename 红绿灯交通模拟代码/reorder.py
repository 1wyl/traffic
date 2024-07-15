def reorder(cars):    
    L = len(cars)
    index = []
    for i in range(L):
        index += [i]
    newcars = []
    newcars2 = []
    while index != []:
        record = []
        for i in range(len(index)):
            if i == 0:
                newcars += [cars[index[i]]]
                record += [0]
            elif cars[index[i]].direction == newcars[-1].direction and cars[index[i]].coordinate == newcars[
                -1].coordinate and cars[index[i]].serial == newcars[-1].serial:
                newcars += [cars[index[i]]]
                record += [i]
        cardisstoplines = []
        for i in record:
            cardisstoplines += [cars[index[i]].disstopline]
        ordered_list = sorted(range(len(cardisstoplines)), key=lambda k: cardisstoplines[k])  # 获取索引排序
        cars[index[ordered_list[0]]].d_c=None
        cars[index[ordered_list[0]]].d_v = None
        for i in ordered_list:
            newcars2 += [cars[index[i]]]
        record.reverse()
        for number in record:
            index.pop(number)
    return newcars2