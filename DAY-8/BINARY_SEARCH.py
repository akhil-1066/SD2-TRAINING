def BinSearch(l,num,s,e):
    if s<=e:
        mid=(s+e)//2
        if l[mid]==num:
            return True
        if l[mid]>num:
            return BinSearch(l,num,s,mid-1)
        else:
            return BinSearch(l,num,mid+1,e)
    return False
l=list(map(int,input().split()))
print(BinSearch(l,int(input()),0,len(l)-1))