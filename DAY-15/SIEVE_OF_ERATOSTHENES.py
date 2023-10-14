def Primes(n):
    dp=[1 for _ in range(n+1)]
    for i in range(2,n+1):
        j=2*i
        if dp[i]:
            while j<=n:
                dp[j]=0
                j+=i
    return [i for i in range(2,n+1) if dp[i]]
n=int(input())
print(Primes(n))