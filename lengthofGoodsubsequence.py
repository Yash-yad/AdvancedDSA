def longest_good_subsequence(arr):
    if not arr:
        return 0
    
    count = 1  
    last_parity = arr[0] % 2
    
    for i in range(1, len(arr)):
        if arr[i] % 2 != last_parity:
            count += 1
            last_parity = arr[i] % 2
    
    return count
