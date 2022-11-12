def Softy(n, k, l,c,d,p,nl,np):
    tos1=((k*l)/nl)/n
    tos2=(c*d)/n
    tos3=(p/np)/n
    tos4=min(tos1,tos2,tos3)
    return int(tos4)

n, k, l, c, d, p, nl, np=map(int, input().split())
print(Softy(n, k, l, c, d, p, nl, np))

