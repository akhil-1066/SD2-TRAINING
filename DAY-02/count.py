matrix=[]
for i in range(int(input("Enter the value n:"))):
    matrix.append(list(map(int,input().split())))
o=[0,0,0,0]
z=[0,0,0,0]
n=len(matrix)
matrix1=list(zip(*matrix))
for i in range(n):
    v=sum([j for j in matrix[i]])
    if v==n:
        o[0]+=1
    elif v==0:
        z[0]+=1
    v=sum([j for j in matrix1[i]])
    if v==n:
        o[1]+=1
    elif v==0:
        o[1]+=1
s=0
s1=0
for i in range(n):
    s+=matrix[i][i]
    s1+=matrix[i][n-i-1]
if s==n:
    o[2]=1
elif s==0:
    z[2]=1
if s1==n:
    o[3]=1
elif s1==0:
    z[3]=1
print("1's vertical count: ",o[0])
print("1's Horizontal count: ",o[1])
print("1's right diagonal count: ",o[2])
print("1's left diagonal count: ",o[3])
print("0's vertical count: ",z[0])
print("0's Horizontal count: ",z[1])
print("0's right diagonal count: ",z[2])
print("0's left diagonal count: ",z[3])