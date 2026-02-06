n=int(input())
numbers=list(map(int,input().split()))
for i in range(n):
    numbers[i]*=numbers[i]
for i in numbers:
    print(i,end=" ")