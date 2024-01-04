import sys;input=sys.stdin.readline

n = int(input())

points = list(map(int, input().split()))

sortedPoints = sorted(points)
sortedPoints = list(dict.fromkeys(sortedPoints))
def binSearch(arr, s, e, key):
    if s > e:
        return -1
    mid = (s+e) // 2
    if arr[mid] == key: return mid
    elif arr[mid] > key: return binSearch(arr, s, mid-1, key)
    else: return binSearch(arr, mid+1, e, key)

ans = [0] * n
for i in range(n):
    ans[i] = binSearch(sortedPoints, 0, len(sortedPoints)-1, points[i])

print(' '.join(map(str,ans)))