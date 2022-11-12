def f(x):
    if x == 0:
        return 1
    g = int(x / 2)
    v = f(g)
    if x % 2 == 0:
        return v * v % 1000000007
    else:
        return (v * v % 1000000007 * 2) % 1000000007


n = int(input())
i = 0
ans = 0
while i < n:
    j = int(input())
    ans = (j * f(j - 1)) % 1000000007
    print("Case #%d: %d" % (i + 1, ans))
    i += 1
