l=list(map(int,input().split()))
l.sort()
target=int(input())
i=0;j=1
s=l[i]+l[j]
while i<len(l) and j<len(l):
    if s==target:
        print(l[i:j+1])
        break
    elif target>s:
        j+=1
        s+=l[j]
    else:
        s-=l[i]
        i+=1
else:
    print(None)