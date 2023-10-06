l=list(map(int,input().split()))
n=len(l)
counter=[]
for i in range(10):
    counter.append(l.count(i))
counter1=counter.copy()
for i in range(1,10):
    counter[i]+=counter[i-1]
sortl=[0 for i in range(n)]
for i in range(9,-1,-1):
    for j in range(counter1[i]):
        counter[i]-=1
        l[counter[i]]=i
print(l)