s=input()
s1=input()
substring=''
for i in range(len(s1)):
    Subs=''
    for j in range(i,len(s1)):
        Subs+=s1[j]
        if Subs in s and len(substring)<len(Subs):
            substring=Subs
print(substring)