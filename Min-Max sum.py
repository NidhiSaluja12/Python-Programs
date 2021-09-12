def miniMaxSum(arr):
    
    res = []
    
    for i in range(len(arr)):
        sum1 = sum(arr)-arr[i]
        res.append(sum1)
    min1 = min(res)
    max1 = max(res)
    print(min1,max1,sep=' ')
        
 

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)

