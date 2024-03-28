# https://www.acmicpc.net/problem/13022
import sys
def check(s, e, w):
    #print(s, e, w)
    tmpw = 0
    tmpo = 0
    tmpl = 0
    tmpf = 0
    tmpword = 'w'
    index = 0
    for widx in range(s, e+1):# wwoollff
        if tmpword != word[widx]:
            index += 1
            if word[widx] != wolf[index%4]:
                print(0)
                sys.exit()
        tmpword = word[widx]
        if word[widx] == 'w':
            tmpw += 1
        if word[widx] == 'o':
            tmpo += 1
        if word[widx] == 'l':
            tmpl += 1
        if word[widx] == 'f':
            tmpf += 1
    if tmpw == tmpo == tmpl == tmpf == w:
        return True
    else: 
        return False
        
word = list(input()) # wolfwwoollff
wolf = ['w', 'o', 'l', 'f']

tmp = 'w'
st = 0
wcnt = 0
for widx in range(len(word)):
    if word[widx] == 'w':
        wcnt += 1
    if widx == len(word)-1:
        if word[widx] != 'f':
            print(0)
            sys.exit()
        end=widx
        if check(st, end, wcnt) is False:
            print(0)
            sys.exit()
        st = widx    
        wcnt = 0
    elif tmp == 'f' and word[widx] == 'w':
        end = widx-1
        if check(st, end, wcnt-1) is False:
            print(0)
            sys.exit()
        st = widx
        wcnt = 1
    tmp = word[widx]
print(1)