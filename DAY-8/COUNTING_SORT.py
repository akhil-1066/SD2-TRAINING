l=list(map(int,input().split()))
n=len(l)
counter=[0 for i in range(10)]
for i in range(n):
    counter[l[i]]+=1
for i in range(1,10):
    counter[i]+=counter[i-1]
sortl=[0 for i in range(n)]
for i in l[::-1]:
    counter[i]-=1
    l[counter[i]]=i
print(l)