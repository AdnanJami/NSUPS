import math
n,k = input().split()
i=0
count=0
while i<int(n):
    t=int(input())
    if t%int(k)==0:
        count+=1


    i+=1
print(count)