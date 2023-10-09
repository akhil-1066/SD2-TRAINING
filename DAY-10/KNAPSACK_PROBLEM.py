def Knapsack(items,l,capacity):
    if(capacity>sum(items)):
        return "NO SUFFICIENT ITEMS!"
    i=0
    profit=0
    while capacity:
        if capacity<=l[i][0]:
            profit+=capacity*l[i][2]
            break
        print(l[i][1])
        profit+=l[i][1]
        capacity-=l[i][0]
        i+=1
    return profit

items=list(map(int,input().split()))
profits=list(map(int,input().split()))
profit_per_unit=[]
for i in range(len(items)):
    profit_per_unit.append(profits[i]/items[i])
capacity=int(input()) 
l=list(zip(items,profits,profit_per_unit))
l.sort(key=lambda x:x[2],reverse=True)
l=[list(i) for i in l]
#print(l)
print(Knapsack(items,l,capacity))