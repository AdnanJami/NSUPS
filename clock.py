m, n = input().split(':')
m1, n1 = input().split(':')
m = int(m)
m1 = int(m1)
n = int(n)
n1 = int(n1)
x3 = (((m * 60 + n) + (m1 * 60 + n1)) / 2) / 60
y3 = (((m * 60 + n) + (m1 * 60 + n1)) / 2) % 60
if x3 >= 10:
    if y3 >= 10:
        print("%d:%d" % (x3, y3))
    else:
        print("%d:0%d" % (x3, y3))

else:

    if y3 >= 10:
        print("0%d:%d" % (x3, y3))
    else:
        print("0%d:0%d" % (x3, y3))
