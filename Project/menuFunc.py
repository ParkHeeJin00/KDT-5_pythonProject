
file = 'fooddata.txt'

wholefood = []
foodC = {}
foodK = {}
foodS = {}
foodCDict = {}
key = ''

with open(file,mode='r',encoding='utf-8') as f:
    datas = f.readlines()
    for data in datas:
        if data =='endw\n':break
        wholefood.append(data[:-1])
    flag = 0
    k = 1
    for data in datas:
        if data == 'endw\n':
            flag = 1
        elif flag:
            if data == 'endc\n': break
            if data[0] == 'c':
                key = data[1:-1]
                foodC[key] = []
                foodCDict[k] = key
                k +=1
            else:
                foodC[key].append(data[:-1])

    flag = 0
    for data in datas:
        if data == 'endc\n':
            flag = 1
        elif flag:
            if data == 'endk\n': break
            if data[0] == 'k':
                key = data[1:-1]
                foodK[key] = []
            else:
                foodK[key].append(data[:-1])
    flag = 0
    for data in datas:
        if data == 'endk\n':
            flag = 1
        elif flag:
            if data == 'ends\n': break
            if data[0] == 's':
                key = data[1:-1]
                foodS[key] = []
            else:
                foodS[key].append(data[:-1])



print(wholefood)
print(foodC)
print(foodK)
print(foodS)
print(foodCDict)