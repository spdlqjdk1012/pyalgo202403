def whowin(tmp):
    #print("w",tmp)
    xwin = 0
    owin = 0
    if tmp[0] == tmp[1] == tmp[2] and tmp[0] != '.':
        if tmp[0] == 'X':   xwin+=1
        elif tmp[0] == 'O':   owin+=1
    if tmp[3] == tmp[4] == tmp[5] and tmp[3] != '.':
        if tmp[3] == 'X':   xwin+=1
        elif tmp[3] == 'O':   owin+=1
    if tmp[6] == tmp[7] == tmp[8] and tmp[6] != '.':
        if tmp[6] == 'X':   xwin+=1
        elif tmp[6] == 'O':   owin+=1
    
    if tmp[0] == tmp[3] == tmp[6] and tmp[0] != '.':
        if tmp[0] == 'X':   xwin+=1
        elif tmp[0] == 'O':   owin+=1
    if tmp[1] == tmp[4] == tmp[7] and tmp[1] != '.':
        if tmp[1] == 'X':   xwin+=1
        elif tmp[1] == 'O':   owin+=1
    if tmp[2] == tmp[5] == tmp[8] and tmp[2] != '.':
        if tmp[2] == 'X':   xwin+=1
        elif tmp[2] == 'O':   owin+=1

    if tmp[0] == tmp[4] == tmp[8] and tmp[0] != '.':
        if tmp[0] == 'X':   xwin+=1
        elif tmp[0] == 'O':   owin+=1
    if tmp[2] == tmp[4] == tmp[6] and tmp[2] != '.':
        if tmp[2] == 'X':   xwin+=1
        elif tmp[2] == 'O':   owin+=1

    if owin>0:  return 'O'
    elif xwin>0: return 'X'
    else: 
        return -1
    
while True:
    tmp = list(input())
    if tmp[0] == 'e':
        exit()
    xcnt = 0
    ocnt = 0
    for i in tmp:
        if i=='X':
            xcnt+=1
        if i=='O':
            ocnt+=1
    
    result = whowin(tmp)
    #print(xcnt, ocnt, result)
    if result == 'X' and xcnt == ocnt+1:
        print("valid")
        continue
    if result == 'O' and xcnt == ocnt:
        print("valid")
        continue
    if result == -1:
        if ocnt+1 == xcnt and xcnt+ocnt==9:
            print("valid")
        else: print("invalid") 
    else:
        print("invalid")     



"""
1) X가 이길경우    X가 1칸 더 많아야함
2) O가 이길경우  X와 동일함
3) 무승부일 경우(승자가 없을 경우) X가 한칸더많고 빈칸이 없어야함 
4) X랑O랑 둘다 이긴 경우 무조건 O가 한칸 더 많아야한다
	"어느 때든지 한 사람의 말이 가로, 세로, 대각선 방향으로 3칸을 잇는 데 성공하면 게임은 즉시 끝난다"
	ex) XXXOOOX..    => Invalid

"""