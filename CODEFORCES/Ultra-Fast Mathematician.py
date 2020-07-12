mylist=list(map(int,input()))
mylist2=list(map(int,input()))
for i in range(0,len(mylist)):
    print(mylist[i]^mylist2[i],end='')