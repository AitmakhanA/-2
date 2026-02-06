n=int(input())
numbers=[]
for i in range(n):
    x=input().strip()
    numbers.append(x)
checked=[]
for i in range(n):
    if numbers[i] not in checked:
        checked.append(numbers[i])
checked.sort()
for i in checked:
    print(i,numbers.index(i)+1)
