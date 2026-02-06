n=int(input())
numbers=list(map(int,input().split()))
max=numbers[0]
pos=1
count=1
for i in numbers:
    if i>max:
        max=i
        pos=count
    count+=1
print(pos