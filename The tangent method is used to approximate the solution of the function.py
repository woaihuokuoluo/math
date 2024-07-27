def A(n):
    return n**5+5*n+1       #Objective function

def B(n):
    return 5*n**4+5          #The derivative of the objective function

a = -1
b = 0    #Quarantine Zone
c = 0
while a!=c:
    c = round(a,3)
    a = round(a - A(a)/B(a),3)
else:
    print(a)

