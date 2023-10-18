l=list(map(int,input().split()))
m=max(l)
print()
for i in range(m,0,-1):
    print(f'{i:2d}',end='|')
    for val in l:
        if val>=i:
            print('x ',end='')
        else:
            print('  ',end='')
    print()
print('   ',end='')
for i in l:
    print('-',end=' ')
print()
print('   ',end='')
for i in l:
    print(i,end=' ')