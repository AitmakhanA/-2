n=int(input())
numbers=list(map(int,input().split()))
max=numbers[0]
for i in numbers:
    if i>max:
        max=i
print(max)