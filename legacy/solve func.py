a, b, c = map(float, input().split())
delta = (b**2 - 4*a*c)
if delta >= 0:
    x1: float = (delta**0.5-b)/2*a
    x2: float = -(delta**0.5+b)/2*a
    if x1 > x2:
        print("{:.2f} {:.2f}".format(x1, x2))
    else:
        print("{:.2f} {:.2f}".format(x2, x1))
else:
    print("No")
