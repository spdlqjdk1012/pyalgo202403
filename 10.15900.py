# https://www.acmicpc.net/problem/15900
import sys
sys.setrecursionlimit(10**5)
N = int(sys.stdin.readline().rstrip())

graph = [[] for _ in range(N+1)]
visited = [False] * (N+1)

for _ in range(N-1):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

result = 0
def dfs(depth, node):
    isLeaf = True
    global result
    visited[node] = True
    for next in graph[node]:
        if visited[next] is False:
            dfs(depth+1, next)
            isLeaf = False
    if isLeaf is True:
        result +=depth
dfs(0, 1)
#print(result)
if result % 2 == 0:
    print("No")
else:
    print("Yes")

    #https://imzzan.tistory.com/45
    #https://www.acmicpc.net/board/view/136846