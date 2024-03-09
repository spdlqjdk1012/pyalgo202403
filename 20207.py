num = int(input())
mylist = []
for i in range(num):
    tmp = list(map(int, input().split()))
    
    mylist.append(tmp)
mylist.sort(key=lambda x:x[0])
#print(mylist)

for tmp in mylist:
    diff = tmp[1]-tmp[0]+1
    tmp.append(diff)
#print(mylist)

mylist.sort(key=lambda x:x[-1], reverse=True)
print(mylist)