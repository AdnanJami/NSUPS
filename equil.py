T = int(input())
i = 0
sumA=0
sumB=0
sumC=0
while i < T:
    a,b,c=map(int,input().split())
    sumA=sumA+a
    sumB=sumB+b
    sumC=sumC+c
    i += 1
if sumA==0 and sumC==0 and sumB==0:
    print("YES")
else:
    print("NO")