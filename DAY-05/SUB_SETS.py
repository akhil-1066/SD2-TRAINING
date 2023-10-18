def Subsets(l):
    res=[]
    ans=[]
    def subsetsprint(res,l,ans):
        if len(l)==0:
            ans.append(res)
            return ans
        ans = subsetsprint(res+[l[0]],l[1:],ans)
        ans = subsetsprint(res,l[1:],ans)
        return ans
    return subsetsprint(res,l,ans)

l = [1,2,3,4]
print(Subsets(l))