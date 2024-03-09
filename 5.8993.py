#https://www.acmicpc.net/problem/8983

def bsearch(a, b):
    start = 0
    end = len(Llist)-1

    while start <= end:
        mid = (start+end) // 2

        if getL(mid, a, b) <= L:
            return True
        
        if getL(mid, a, b)
def getL(x, a, b):
    xa = x-a
    if xa <0 :
        xa = xa*-1
    return xa+b

M, N, L = map(int, input().split())
Llist = list(map(int, input().split()))
Llist.sort()
for i in range(N):
    a, b = map(int, input().split())
    # 사정거리 확인 
    bsearch(a, b)