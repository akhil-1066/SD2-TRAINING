for i in range(100):
    n=i
    while n>9:
        n=sum([int(j) for j in str(n)])
    if n==1:
        print(i)
