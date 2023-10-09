print(*[i for i in range(10000) if sum([int(j) for j in str(i**2)])==i])
