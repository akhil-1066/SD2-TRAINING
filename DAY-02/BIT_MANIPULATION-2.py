n=int(input())
l=list(map(int,input().split()))
for i in range(n+1):
    if i not in l:
        print(i)
        break
