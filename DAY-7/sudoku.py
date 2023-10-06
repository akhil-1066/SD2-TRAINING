def valid_num(l,i,j,num):
    r=i//3
    j=j//3
    t=[row[j:j+3] for row in l[i:i+3]]
    t1=[]
    for i in t1:
        t1+=i
    x=[]
    for i in t1:
        x+=i
    t2=[row[j:j+1] for row in l]
    if num not in t1 and num not in l[i] and num not in t2:
        return True
    return False
def Sudoku(l,i,j):
    if i>8 and j>8:
        return True
    if not l[i][j]:
        for num in range(1,10):
            if l[i][j]==valid_num(l,i,j,num):
                l[i][j]=num
                if Sudoku(l,i+1,j) and Sudoku(l,i,j+1):
                    return True
        return False
    Sudoku(l,i+1,j)
    Sudoku(l,i,j+1)
l=[]
for i in range(9):
    l.append(list(map(int,input().split())))
Sudoku(l,0,0)
for i in l:
    print(*i)