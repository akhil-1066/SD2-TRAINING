def qsorting(l,start,end):
    pivot=l[end]
    i=start-1
    for j in range(start,end):
        if l[j]<pivot:
            i=i+1
            l[j],l[i]=l[i],l[j]
        l[i+1],l[end]=l[end],l[i+1]
        return i+1
def quick(l,start,end):
    if start<end:
        pivot=qsorting(l,start,end)
        quick(l,start,end-1)
        quick(l,end,pivot-1)
        quick(l,pivot+1,end)
l=list(map(int,input().split()))
quick(l,0,len(l)-1)
print(l)