mylist=list(map(int,input().split()))
a=0
b=min(mylist[:4:]) - mylist[4]
if(b>=0):
    a=min(b,mylist[5]-mylist[4]+1)
print(a)