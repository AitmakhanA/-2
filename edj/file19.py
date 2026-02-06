n=int(input())
episodes=[]
for i in range(n):
    s,k=input().split()
    k=int(k)
    episodes.append((s,k))
totals=[]
for s,i in episodes:
    if s not in [x[0] for x in totals]:
        total=0
        for name,k in episodes:
            if name==s:
                total+=k
        totals.append((s,total))
for i in range(len(totals)):
    for j in range(i+1,len(totals)):
        if totals[i][0]>totals[j][0]:
            totals[i],totals[j]=totals[j],totals[i]
for s,total in totals:
    print(s,total)