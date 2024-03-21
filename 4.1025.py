#완전제곱수란 1부터 연속된 홀수의 합 1+3+5=9
def isSquareNum(num):
    odds = 1
    while num > 0:
        num = num-odds
        odds += 2
        if num == 0:
            return True
    return False

#n = int(input())
#print(isSquareNum(n))

result = -1
row, col = map(int, input().split())
arr = []
for i in range(row):
    tmplist = list(map(int, input()))
    arr.append(tmplist)
#5x5
for r in range(row): #행   012
    for c in range(col): #열 0123
        for rm in range(-row, row): # 행등차 -2~2   
            for cm in range(-col, col): # 열등차 -3~3
                print(r, c, rm, cm)
                num = ''
                tmpr = r
                tmpc = c
                while 0<=tmpr<row and 0<=tmpc<col:
                    num += str(arr[tmpr][tmpc])
                    print("----",tmpr, tmpc, num)
                    # (0,0)(1,0)(2,0)(3,0)(4,0)
                    # (0,0)(1,1)(2,2)(3,3)(4,4)
                    # (0,0)(1,2)(2,4)
                    # (0,0)(1,3)
                    # (0,0)(1,4)
                        #...
                    # (0,0)(4,0)
                    # (0,0)(4,1)
                    if isSquareNum(int(num)) is True:
                        result = max(int(num), result)
                    tmpr += rm
                    tmpc += cm
print(result)