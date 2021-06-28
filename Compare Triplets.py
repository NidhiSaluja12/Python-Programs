def compareTriplets(a, b):
    A_length = len(a)
    B_length = len(b)
    A_points = 0
    B_points = 0
    for i in range(A_length):
        if a[i]>b[i]:
            A_points+=1
        elif a[i]<b[i]:
            B_points+=1
    return A_points,B_points
            
  

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    result = compareTriplets(a, b)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
