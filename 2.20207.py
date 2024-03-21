num = int(input())
calendar = [0 for i in range(366)]
for i in range(num):
    st, end = map(int, input().split())
    for num in range(st, end+1):
        calendar[num] = calendar[num]+1
#print(calendar) 

start = 0
end = 0
maxval = 0
width = []
for i in range(len(calendar)):
    if calendar[i] != 0:
        if start == 0:
            start = i
        maxval = max(maxval, calendar[i])

    if calendar[i] == 0: 
        if start != 0 and end == 0:
            end = i
            w = (end-start) * maxval
            #print(w)
            width.append(w)
            start = 0
            maxval = 0
            end = 0

    if i == len(calendar)-1:
        w = (i-start+1) * maxval
        width.append(w)
#print(width)
print(sum(width))


"""
5
1 3
2 4
5 7
9 11
13 13
18


1
1 365
# 답 : 365
"""