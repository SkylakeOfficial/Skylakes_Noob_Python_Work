
def ch2int(li):
    ret = []
    for i in li:
        ret.append(int(i))
    return ret
# 把列表中的字符串转化为整数


def out(li):
    for i in li:
        print(-i[0], end=' ')
        print(i[1])
# 打印结果，为方便排序，有一个值用相反数存储


n = input()
ipt = ch2int(input().split())
MyCount = {}
for WDNMD in ipt:
    if -WDNMD in MyCount:
        MyCount[-WDNMD] += 1
    else:
        MyCount[-WDNMD] = 1

MyCount2 = sorted(list(MyCount.items()), key=(lambda x: [x[1], x[0]]), reverse=True)

out(MyCount2)
