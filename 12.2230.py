# https://www.acmicpc.net/problem/2230
import sys
N, M = map(int, sys.stdin.readline().split())
#print(N, M)
arr = []
for i in range(N):
    num = int(sys.stdin.readline().rstrip())
    arr.append(num)

arr.sort()
#print(arr)
result = 100000000000
left, right = 0, 1
while right<N:
    tmp = arr[right]-arr[left]
    if tmp == M:
        print(tmp)
        sys.exit()
    elif tmp < M:
        right += 1
    else:
        left += 1
        result = min(result, tmp)
print(result) 
# 1 2 3 5 8 13

"""
7 4
1
8
15
16
17
18
22
"""