from sys import stdin
x= int(input())
y= int(input())
i=0
while i <x:
    a=list(map(int,input().split()))
    mn=min(a)
    a.remove(mn)
    mn1=min(a)
    sum=mn+mn1
    print(sum)