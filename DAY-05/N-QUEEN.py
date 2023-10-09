def Nqueen(n):
    col=[]
    posd=[]
    negd=[]
    ans=[]
    board=[['.']*n for _ in range(n)]
    def backtracking(r):
        if r==n:
            l=[''.join(i) for i in board]
            ans.append(l)
            return
        for c in range(n):
            if c in col or (r+c) in posd or (r-c) in negd:
                continue
            board[r][c]='Q'
            col.append(c)
            posd.append(r+c)
            negd.append(r-c)
            
            backtracking(r+1)
            
            board[r][c]='.'
            col.remove(c)
            posd.remove(r+c)
            negd.remove(r-c)
    backtracking(0)
    return ans
print(Nqueen(4))