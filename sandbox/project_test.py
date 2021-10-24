def minDeletions(arr):
    c = 0
    i = 0
    n = len(arr)-1

    while i < n:
        if arr[i] > arr[i+1]:
            c += 1
            arr.remove(arr[i+1])
            i -= 1
            n -= 1
        i += 1

    c = c - 1
    if c < 0:
        c = 0
    return c