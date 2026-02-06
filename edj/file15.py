n=int(input())
names=[]
for i in range(n):
    name=input().strip()
    if name not in names:
        names.append(name)
print(len(names))