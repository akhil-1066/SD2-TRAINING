def QuickSort(l,low,high):
    if low<high:
        i=low
        pivot=low
        j=high
        while i<j:
            while l[i]<=l[pivot] and i<high:
                i+=1
            while l[j]>l[pivot] and j>=0:
                j-=1
            if i<j:
                l[i],l[j]=l[j],l[i]
        l[pivot],l[j]=l[j],l[pivot]
        QuickSort(l,low,j-1)
        QuickSort(l,j+1,high)
l=list(map(int,input().split()))
n=len(l)
QuickSort(l,0,n-1)
print(l)