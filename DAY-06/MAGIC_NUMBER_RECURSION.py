def matrix(mat,n,i,j,num):
        if num<=n**2:
            while True:
                i,j=i%n,j%n
                if mat[i][j]:
                    i,j=i+1,j-2
                    continue
                mat[i][j]=num
                break
            matrix(mat,n,i-1,j+1,num+1)
def magic_matrix(n):
    mat=[[0 for i in range(n)] for j in range(n)]
    i,j=n//2,n-1
    mat[i][j]=1
    matrix(mat,n,i-1,j+1,2)
    return mat
n=int(input())
print('MAGIC CONSTATNT',n*(n**2 +1)//2)
for row in magic_matrix(n):
    print(*row)