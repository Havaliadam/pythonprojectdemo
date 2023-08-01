def maxProductSubset(arr , n):
    max_neg = -9999999
    count_neg = 0
    count_zero = 0
    prod = 1

    for i in range ( n ):

        if arr[i] == 0:
            count_zero += 1
            continue

        if arr[i] < 0:
            count_neg += 1
            max_neg = max ( max_neg ,
                            arr[i] )

        prod = prod * arr[i]

    if count_zero == n:
        return 0

    if count_neg & 1:

        if (count_neg == 1 and count_zero > 0 and
                count_zero + count_neg == l):

            return 0
        else:
            prod = int ( prod / max_neg )

    return prod


arr = [-1 , -1 , -2 , 4 , 3]
n = len ( arr )
print ( maxProductSubset ( arr ,
                           n ) )