
import sys
input = sys.stdin.read
data = input().split()

idx = 0
t = int(data[idx])
idx += 1

results = []

for _ in range(t):
    n = int(data[idx])
    idx += 1
    
    arr = list(map(int, data[idx:idx + n]))
    idx += n
    
    q = int(data[idx])
    idx += 1
    
    queries = []
    for __ in range(q):
        pos = int(data[idx]) - 1
        val = int(data[idx + 1])
        queries.append((pos, val))
        idx += 2
    
    def find_unsorted_bounds(arr):
        left = 0
        while left < n - 1 and arr[left] <= arr[left + 1]:
            left += 1
        if left == n - 1:
            return -1, -1
        right = n - 1
        while right > 0 and arr[right] >= arr[right - 1]:
            right -= 1
        return left, right
    
    l, r = find_unsorted_bounds(arr)
    
    results.append(f"{l + 1} {r + 1}" if l != -1 else "-1 -1")
    
    for pos, val in queries:
        arr[pos] = val
        if l == -1:
            l, r = find_unsorted_bounds(arr)
        else:
            if pos <= l:
                l = max(0, pos - 1)
            if pos >= r:
                r = min(n - 1, pos + 1)
            while l > 0 and arr[l - 1] > arr[l]:
                l -= 1
            while r < n - 1 and arr[r] > arr[r + 1]:
                r += 1
            if arr[l] <= arr[l + 1] and arr[r] >= arr[r - 1]:
                l, r = find_unsorted_bounds(arr)
        
        results.append(f"{l + 1} {r + 1}" if l != -1 else "-1 -1")

sys.stdout.write("\n".join(results) + "\n")

