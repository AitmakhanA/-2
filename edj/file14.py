n=int(input())
numbers=list(map(int,input().split()))
maxcount=0
mostfreq=numbers[0]
for i in numbers:
    count=0
    for j in numbers:
        if i==j:
            count+=1
    if (count>maxcount) or (count==maxcount and i<mostfreq):
        maxcount=count
        mostfreq=i
print(mostfreq)