def simpleArraySum(*list):
    sum=0
    for a in list:
        sum += a
    return sum
n = input()
s=list(map(int,input().split()))
print(simpleArraySum(*s))
