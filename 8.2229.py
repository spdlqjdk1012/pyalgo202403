# https://www.acmicpc.net/problem/2229
n = int(input())
arr = list(map(int, input().split())) # 2 5 7 1 3
dp = [0 for _ in range(n)]
for i in range(n):
    maxv = 0
    minv = 10000
    for j in reversed(range(i)):
        maxv = max(maxv, arr[j])
        minv = min(minv, arr[j])
        dp[i] = max(dp[i], dp[j-1]+maxv-minv)
print(dp)

"""
[2] / 5 7 1 3
[0, ...]

[2]  [5] / 7 1 3
[0, 0...]
[2 5] / 7 1 3
[0, 3 ...]

[2 5] [7] /1 3    =>3
[0 , 3, 3...]
[2] [5 7] /1 3    =>2
[0 , 3, 3...]
[2 5 7] /1 3    =>5
[0 , 3, 5...]

https://blog.naver.com/PostView.nhn?blogId=occidere&logNo=221535723529
*다시풀기...
"""