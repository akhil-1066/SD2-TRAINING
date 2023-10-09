def Floorbin(l,num):
    def Search(l,num,first,last):
        if first<=last:
            mid=(first+last)//2
            if l[mid]==num:
                return num
            if l[mid]>num:
                return Search(l,num,first,mid-1)
            return Search(l,num,mid+1,last)
        if first>0:
            return l[first-1]
        return -1
    return Search(l,num,0,len(l)-1)
l=list(map(int,input().split()))
num=int(input())
print(Floorbin(l,num))