# https://www.acmicpc.net/problem/1647
# 최소스패닝트리 -> 크루스칼 알고리즘(순환체크unionfind)
import sys
def find(x):
    if parent[x] != x:# x가1일 경우 parent[x] = 0 , x가0 find(0)==0 같음 return0 
        parent[x] = find(parent[x])
    return parent[x]

def union(a, b):
    a = find(a)
    b = find(b)
    if a<b:
        parent[b] = a
    else:
        parent[a] = b

N, M = map(int, input().split())
parent = [0] * (N+1)
for i in range(1, N+1):
    parent[i] = i
edges = []
for i in range(M):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    edges.append((a, b, c))
edges.sort(key=lambda x:x[2]) # 가중치가 적은 것부터 정렬

result = 0
maxcost = 0
for a, b, c in edges:
    if find(a) != find(b): #사이클의 존재여부 확인 
        union(a, b)
        result += c
        maxcost = max(maxcost, c)

print(result - maxcost) # 간선의 비용이 가장 큰 경우 마을을 나눈다 

