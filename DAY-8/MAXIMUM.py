def Max(lst,f,l):
    if f<=l:
        mid=(f+l)//2
        a=Max(lst,f,mid-1)
        b=Max(lst,mid+1,l)
        c=lst[mid]
        return a if a>b and a>c else b if b>c else c
    return float('-inf')
lst=list(map(int,input().split()))
print(Max(lst,0,len(lst)-1))