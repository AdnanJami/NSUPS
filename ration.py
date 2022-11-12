r = int(input())
i= 0
while i < r:
    a, b = map(int, input().split())
    if a > b:
        print(">")
    elif a < b:
        print("<")
    else:
        print("=")
    i+=1