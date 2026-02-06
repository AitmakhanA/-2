n=int(input())
numbers=list(map(int,input().split()))
arr=[]
for i in numbers:
    if i in arr:
        print("NO")
    else:
        print("YES")
        arr.append(i)