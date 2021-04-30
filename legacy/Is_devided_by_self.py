The_number = int(input())
nums = []


def SelfDivisor (num):
    ints = list(str(num))
   # print(ints)#抄的，分解各位，不知道怎么做到的
    for i in ints:
        i = int(i)
        if i == 0:
            return 0
        if num % i != 0:    #打了井号发现好像没有什么好注释的
            return 0
    return 1


for j in range(The_number):
    if SelfDivisor(j+1):
        print(j+1,end=' ')

for k in nums:
    print(k, end=' ')