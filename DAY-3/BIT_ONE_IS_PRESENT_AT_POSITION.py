num,pos=map(int,input().split())
b=1<<(pos-1)
print(num & b ==b)
