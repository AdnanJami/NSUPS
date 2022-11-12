x = int(input())
z = 0
y = 0
Z = 0
number = [[] * x for i in range(x)]
if 1 <= x <= 1000:
    while z < x:
        A = list(map(int, input().split()))
        for num in A:
            if 1 <= num <= 1000000:
                pass
            else:

                y += 1
        if y == 0:
            number.append(A)
            z += 1
        else:
            print("Unable to test")
            y = 0
else:
    print("Unable to test")
res = list(filter(None, number))
# print(res)
while Z < x:
    A = res[Z]
    mx = max(A)
    mn = min(A)
    A.remove(mn)
    A.remove(mx)
    A = ''.join(str(x) for x in A)
    print(A)
    Z += 1
