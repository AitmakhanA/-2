n=int(input())
numbers=[]
for i in range(n):
    x=int(input().strip())
    numbers.append(x)
count=0
checked=[]
for i in numbers:
    if i not in checked:
        if numbers.count(i) == 3:
            count += 1
        checked.append(i)
print(count)