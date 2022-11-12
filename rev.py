x= int(input())
for i in range(x):
    rev = 0
    num = int(input())
    while(num):
        rem= num%10
        rev=rev*10+rem
        num=int(num/10)
    print(rev)