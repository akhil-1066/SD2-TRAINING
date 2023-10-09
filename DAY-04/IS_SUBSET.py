def is_subset(l,target,n):
    if not target:
        return True
    if not n:
        return False
    if l[n-1]>target:
        return is_subset(l,target,n-1)
    return is_subset(l,target-l[n-1],n-1) or is_subset(l,target,n-1)
l=list(map(int,input().split()))
print(is_subset(l,int(input()),len(l)))