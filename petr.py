n, wps = int(input()), list(map(int, input().split()))
i, sm = 0, 0
while sm < n:
    if i == 7:
        i = 1
    else:
        i += 1
    sm += wps[i - 1]
print(i)
