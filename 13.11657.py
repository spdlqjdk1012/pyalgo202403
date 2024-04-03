# https://www.acmicpc.net/problem/11657
INF = int(1e9)

V, E = map(int, input().split()) #V노드의수3, E간선의수4

edges = []
dist = [INF]*(V+1)
for i in range(E):
    st, end, diff = map(int, input().split())
    edges.append((st, end, diff))

#print(dist)
#print(edges)

def bellmanFord(st):
    dist[st] = 0# 1번노드에서 1번노드로 이동하는비용 0
    for i in range(V):# 0번노드부터 모든 노드 탐색
        for j in range(E): # 모든 간선 확인
            curNode, edgeNode, cost = edges[j]
            #1번노드에서 2번노드로 이동하는 비용4
            if dist[i] != INF and dist[curNode]+cost<dist[edgeNode]:
                dist[edgeNode] = dist[curNode]+cost
                #print(dist)
                if i == V-1:
                    return True
    return False

result = bellmanFord(1)
#print(dist)
if result is True:
    print(-1)
else:
    for i in range(2, V+1):
        if dist[i] == INF:# 간선이 없는 경우
            print(-1)
        else:
            print(dist[i])
# 1번->2번노드로 가는길 갱신 1->2번거쳐서 ->3번노드로 가는길 갱신 ... 
