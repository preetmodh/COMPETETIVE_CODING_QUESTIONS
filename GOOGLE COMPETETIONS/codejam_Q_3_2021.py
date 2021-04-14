from itertools import permutations

def cost(a):
    ans=0
    for i in range(len(a)-1):
        m=min(a[i:len(a)])
        ind=a.index(m)+1
        if a[i]==m:
            ans+=1
        else:
            ans+=ind - i
            a[i:ind]=reversed(a[i:ind])
    return ans

def findlist(n,c):
    l = list(permutations(range(1, n+1)))
    ans=-1
    for i in range(len(l)):
        if cost(list(l[i]))==c:
            return l[i]
    return ans
    



for t in range(int(input())):
    n,c=map(int,input().split())
    s=sum(range(3,n+1)) + 3
    ans=findlist(n,c)
    if ans==-1:
        print("Case #"+str(t+1)+": "+str("IMPOSSIBLE"))
    else:
        ans=' '.join(map(str,ans))
        print("Case #"+str(t+1)+": "+str(ans))










""" for t in range(int(input())):
    n,c=map(int,input().split())
    a=list(range(1,n+1))
    s=sum(range(3,n+1)) + 3
    if c<n-1 or c>=s:
        print("Case #"+str(t+1)+": "+str("IMPOSSIBLE"))
    elif c==n-1:
        ans=' '.join(map(str,a))
        print("Case #"+str(t+1)+": "+str(ans))
    else:
        d=c-n+2
        a[len(a)-d:len(a)]=reversed(a[len(a)-d:len(a)])
        ans=' '.join(map(str,a))
        print("Case #"+str(t+1)+": "+str(ans)) """
