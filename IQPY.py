def iq_test(x, py):
    y = py.split()
    i = 0
    even = 0
    pos = 0
    eve = 0
    while i < int(x):
        if int(y[i]) % 2 == 0:
            even += 1
            if even > 1:
                eve = 1
        i += 1
    i = 0
    if eve == 1:
        while i < int(x):
            if int(y[i]) % 2 == 0:
                even = 1
            else:
                pos = i
            i += 1

    else:
        while i < int(x):
            if int(y[i]) % 2 != 0:
                odd = 1
            else:
                pos = i
            i += 1
    return pos + 1


x = input()
py = input()

print(iq_test(x, py))
