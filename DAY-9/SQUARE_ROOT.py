def Sqrt(n):
    def Sroot(i,j):
        if j-i!=1:
            mid=(i+j)//2
            if mid*mid==n:
                return mid
            if mid*mid>n:
                return Sroot(i,mid)
            else:
                return Sroot(mid,j)
        return i
    if n<=1:
        return n
    return Sroot(0,n)
n=int(input())
print(Sqrt(n))