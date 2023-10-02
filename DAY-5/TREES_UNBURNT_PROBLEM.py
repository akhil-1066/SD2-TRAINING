import time as t
def is_island(mat,i,j,n):
    if (i>=n or i<0 or j>=n or j<0):
        return
    if not mat[i][j]:
        return
    mat[i][j]=0
    is_island(mat,i,j+1,n)
    is_island(mat,i+1,j,n)
    is_island(mat,i,j-1,n)
    is_island(mat,i-1,j,n)
mat=[]
n=int(input())
for i in range(n):
    mat.append(list(map(int,input().split())))
i,j=map(int,input().split())
s=t.time()
if mat[i][j]:
    is_island(mat,i,j,n)
c=0
for i in mat:
    c+=sum(i)
e=t.time()
print(c)