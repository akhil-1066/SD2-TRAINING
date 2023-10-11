l=list(map(int,input().split()))
left=0
right=len(l)-1
i=0
while i<=right:
    if l[i]==0:
        l[i],l[left]=l[left],l[i]
        left+=1
        i+=1
    elif l[i]==1:
        i+=1
    else:
        l[i],l[right]=l[right],l[i]
        right-=1
print(l)