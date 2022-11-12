T = int(input())
i = 0
while i < T:
    count = 0
    A, B = map(int, input().split())
    C = (B - A) + 1
    num = str(A)
    while A <= B:
        num = str(A)
        A = 0
        if num.find('0') > 0:
            count += 1
        A = int(num)
        A += 1
    print('%d/%d' % (count, C))
    i += 1
