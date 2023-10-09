def quickSort(l):
    if len(l)<=1:
        return l
    pivot=l[0]
    left=[i for i in l if i<pivot]
    right=[i for i in l if i>pivot]
    return quickSort(left)+[pivot]+quickSort(right)
l=list(map(int,input().split()))
print(quickSort(l))