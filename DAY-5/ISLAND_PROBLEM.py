def is_island(mat,i,j,n):
    if (i>=n or i<0 or j>=n or j<0):
        return
    if not mat[i][j]:
        return
    mat[i][j]=0
    is_island(mat,i,j+1,n)
    is_island(mat,i+1,j,n)
    is_island(mat,i,j-1,n)
mat=[]
n=int(input())
c=0
for i in range(n):
    mat.append(list(map(int,input().split())))
for i in range(n):
    for j in range(n):
        if mat[i][j]:
            c+=1
            is_island(mat,i,j,n)
print(c)
'''4 
1 0 0 1
1 0 1 0 
0 1 0 1 
1 0 1 1 6'''
