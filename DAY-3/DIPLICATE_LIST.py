l=list(map(int,input().split()))
l1=[l[0]]
for i in l:
    x=1
    for j in l1:
        if not i^j:
            x=0
            break
    if x:
        l1.append(i)
print(l1)
