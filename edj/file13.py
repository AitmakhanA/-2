from math import sqrt
n=int(input())
if n<=1:
    print("No")
else:
    isprime=True
    for i in range(2,int(sqrt(n))+1):
        if n%i==0:
            isprime=False;
            break
    if isprime:
        print("Yes")
    else:
        print("No")