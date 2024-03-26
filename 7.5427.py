#https://www.acmicpc.net/problem/5427
from collections import deque

n = int(input())
posx = [0,0,1,-1]
posy = [1,-1,0,0]
for i in range(n):
    w, h = map(int, input().split())
    array = []
    visited = [[False]*w for _ in range(h)]
    startw = -1
    starth = -1
    fire = []
    for hindex in range(h):
        wlist = list(input())
        for windex in range(w):
            if(wlist[windex] == "@"):
                startw = windex
                starth = hindex
            if(wlist[windex] == "*"):
                fire.append([windex, hindex])
        array.append(wlist)
    
    dq = deque([])
    for x, y in fire:
        dq.append([x, y, '*', 1])
        visited[y][x] = True
    dq.append([startw, starth, '.', 1])
    visited[starth][startw] = True
    
    check = False
    while dq:
        x, y, kind, cnt = dq.popleft()
        if kind=="." and (x == w-1 or x==0 or y == h-1 or y==0):
            check = True
            print(cnt)
            break

        for i in range(4):
            tmpx, tmpy = x+posx[i], y+posy[i]
            if tmpx>=0 and tmpx<w and tmpy>=0 and tmpy<h and visited[tmpy][tmpx] is False and array[tmpy][tmpx] == ".":
                if kind == "*":
                    dq.append([tmpx, tmpy, '*', cnt+1])
                    visited[tmpy][tmpx] = True
                if kind == ".":
                    dq.append([tmpx, tmpy, '.', cnt+1])
                    visited[tmpy][tmpx] = True
    if check is False:
        print("IMPOSSIBLE")