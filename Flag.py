import math

# pi= 3.1415926
r = int(input())
i = 0
while i < r:
    l = float(input())
    w = l * (6 / 10)
    R = l * (1 / 5)
    Rar = 2 * math.acos(-1) * R
    Sar = (w * l) - Rar
    print("%.2f %.2f" % (Rar, Sar))
    i += 1
