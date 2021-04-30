Mystr = input()
Mystr = list(set(Mystr))
Mystr = sorted(Mystr)
for i in Mystr:
    if i == Mystr[-1]:
        print(i)
    else:
        print(i, end='')