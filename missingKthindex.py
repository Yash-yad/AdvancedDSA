def findKthMissing(arr, k):
    n = len(arr)
    
    def missing(i):
        return arr[i] - (i + 1)
    

    if k > missing(n - 1):
        return arr[-1] + (k - missing(n - 1))
    
    left, right = 0, n - 1
    while left < right:
        mid = (left + right) // 2
        if missing(mid) < k:
            left = mid + 1
        else:
            right = mid
    
    return k + left
