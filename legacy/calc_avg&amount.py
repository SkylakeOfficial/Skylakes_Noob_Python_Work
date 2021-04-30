MyList = []
minus, pos, total = 0, 0, 0
for i in range(10000):
    MyList.append(int(input()))
    if MyList[i] == 0:
        break
del MyList[-1]
for i in MyList:
    total += i
    if i > 0:
        pos += 1
    else:
        minus += 1
print(total / len(MyList))
print(pos)
print(minus)