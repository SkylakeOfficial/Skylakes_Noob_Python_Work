src, tar, start, end = input().split()
start, end = int(start), int(end)
if tar not in src:
    print("none")
else:
    loc = []
    while str.find(src, tar, start, end) != -1:
        loc.append(str.find(src, tar, start, end))
        start += 1
    loc = list(set(loc))
    loc.sort(reverse=False)
    print(",".join(str(x) for x in loc))