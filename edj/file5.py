n=int(input())
integer=n
count=0
while n!=0:
    n//=2
    count+=1
if 2**(count-1)==integer:
    print("YES")
else:
    print("NO")