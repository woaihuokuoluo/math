def A(n):
    return n**3-3*n**2+6*n-1

a = 0
b = 1
while b-a > 0.001:
    x = (a+b)/2
    print(x)
    if A(x)*A(a)>0:
        a = x
    else:
        b = x
else:
    print(a,b)
