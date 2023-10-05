def find_subsets(l):
    def subsets(l):
        if l not in sublist:
            sublist.append(l)
        if not len(l):
            return
        for i in l[::-1]:
            x=[ j for j in l if j!=i]
            subsets(x)
    sublist=[]
    subsets(l)
    return sublist
l=list(map(int,input().split()))
print(find_subsets(l))