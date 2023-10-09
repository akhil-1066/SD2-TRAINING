def Add(lst,f,l):
    if f<=l:
        mid=(f+l)//2
        return lst[mid]+Add(lst,f,mid-1)+Add(lst,mid+1,l)
    return 0
lst=list(map(int,input().split()))
print(Add(lst,0,len(lst)-1))