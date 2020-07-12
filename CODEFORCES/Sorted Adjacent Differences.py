t=int(input())
for _ in range(t):
    input()
    mylist=list(map(int,input().split()))
    mylist.sort()
    
    for i in range(0,len(mylist)):
        print(mylist[len(mylist)//2],end=' ')
        mylist.pop(len(mylist)//2)