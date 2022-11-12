from sys import stdin
import math
T = int(input())
i=0
count=0
while i<T:
    A,B=map(int,input().split())
    gcd=math.gcd(A,B)
    lcm=math.lcm(A,B)
    print(gcd, lcm)
    i+=1
math.tr