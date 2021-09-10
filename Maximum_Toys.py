def MaximumToys(prices, k):
    
    count = 0
    cost = 0

    for price in prices:
        if cost+price <= k:
            count +=1
            cost+=price
            
    return count

n, k = [int(v) for v in input().split()]
prices = sorted([int(v) for v in input().split()])
res = MaximumToys(prices, k)
print(res)
