s=[*input()]
s1=''
n=len(s)
l=[]
l1=[]
for i in range(n):
    if not s[i].isalpha():
        l.append(i)
        l1.append(s[i])
    else:
        s1=s[i]+s1
for i in l:
    s1=s1[:i]+l1[l.index(i)]+s1[i:]
print(s1)
