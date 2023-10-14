l=list(map(int,input().split()))
m=max(l)
print()
for i in range(m,0,-1):
    print(i,end='|')
    for val in l:
        if val==i:
            print('. ',end='')
        else:
            print('  ',end='')
    print()
print('  ',end='')
for i in l:
    print('-',end=' ')
print()
print('  ',end='')
for i in l:
    print(i,end=' ')
