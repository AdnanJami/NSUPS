
def checkSorted(n, arr):

    b = []
    for i in range(n):
        b.append(arr[i])
    b.sort()
    ct = 0
    for i in range(n):
        if arr[i] != b[i]:
            ct += 1

    if ct == 0 or ct == 2:
        return True
    else:
        return False
N=int(input())
P=list(map(int, input().split()))
if checkSorted(N,P):
    print("YES")
else:
    print("NO")