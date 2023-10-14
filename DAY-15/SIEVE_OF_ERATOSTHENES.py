n=int(input())
dp=[1 for _ in range(n+1)]
for i in range(2,n+1):
    j=i
    if dp[i]:
        j+=i
        while j<=n:
            dp[j]=0
            j+=i
print(*[i for i in range(2,n+1) if dp[i]])