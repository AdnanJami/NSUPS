a = list(map(int, input().split()))
i = 0
r = True
while r:
    first = a[0]
    count = 0
    l = 0
    for i in a:
        if first == i:
            count += 1
        else:
            continue
    print(first, count)
    while l < count:
        a.remove(first)
        l += 1

    if len(a) == 0:
        r = False
    else:
        r = True
