def Subset(l,target):
    def is_valid(l,target):
        for k in range(len(l)-2):
            i=k+1
            j=len(l)-1
            while i<j:
                s=l[i]+l[j]+l[k]
                if s==target:
                    return [l[i],l[k],l[j]]
                elif s>target:
                    j-=1
                else:
                    i+=1
    return is_valid(l,target)
l=list(map(int,input().split()))
target=int(input())
print(Subset(l,target))