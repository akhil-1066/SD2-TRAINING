n,b=map(int,input("Enter number and bit:").split())
bn=[*bin(n)[2:]]
l=len(bn)
res=0
if b>=l:
    res=2**b
elif bn[l-b-1]=='1':
    bn[l-b-1]='0'
else:
    bn[l-b-1]='1'
p=0
for i in bn[::-1]:
    res+=int(i)*(2**p)
    p+=1
print(res)
