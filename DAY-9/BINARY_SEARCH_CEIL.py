def Ceilbin(l,num):
    def Search(l,num,first,last):
        if first<=last:
            mid=(first+last)//2
            if l[mid]==num:
                return num
            if l[mid]>num:
                return Search(l,num,first,mid-1)
            return Search(l,num,mid+1,last)
        if last<len(l)-1:
            return l[last+1]
        return -1
    return Search(l,num,0,len(l)-1)
l=list(map(int,input().split()))
num=int(input())
print(Ceilbin(l,num))