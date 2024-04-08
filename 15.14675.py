# https://www.acmicpc.net/problem/14675
import sys
N = int(input()) #5
arr = [0] * (N+1) #[-,0,0,0,0,0] 


for i in range(N-1): #[-,1,2,2,2,1] 
    a, b = map(int, sys.stdin.readline().rstrip().split())
    arr[a] += 1
    arr[b] += 1

q = int(input())
for i in range(q):
    c, d = map(int, sys.stdin.readline().rstrip().split())
    if c==1:
        if arr[d]==1:# 말단 노드만 단절점
            print("no")
        else:
            print("yes")
    if c==2:# 모든 선이 단절선
        print("yes")