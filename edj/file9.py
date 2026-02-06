n=int(input())
numbers=list(map(int,input().split()))
max=numbers[0]
min=numbers[0]
for i in numbers:
    if i>max:
        max=i
    elif i<min:
        min=i
for i in range(n):
    if numbers[i]==max:
        numbers[i]=min
for i in numbers:
    print(i,end=" ")