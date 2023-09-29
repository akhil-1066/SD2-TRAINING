n=int(input())
c=0
while n:
    if not n & (n-1):
        c+=1
    else:
        break
    n=n>>1
if c&1:
    print("Power of 4")
else:
    print("Not a Power of 4")
