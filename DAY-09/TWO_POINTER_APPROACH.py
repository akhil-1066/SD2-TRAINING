def Twosum(l,target):
    left,right=0,len(l)-1
    while left<right:
        sum=l[left]+l[right]
        if sum==target:
            return l[left],l[right]
        if sum>target:
            right-=1
        else:
            left+=1
    return "No Posibility"
l=list(map(int,input().split()))
print(Twosum(l,int(input())))