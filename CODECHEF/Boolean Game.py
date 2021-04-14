for t in range(int(input())):
    n,m,k=map(int,input().split())
    a=list(map(int,input().split()))
    b=[]
    for i in range(m):
        b.append(list(map(int,input().split())))
    ans=[]
    if k!=1:
        for i in range(0,pow(2,n)):
            array=[0]*n
            cost=0
            for j in range(n):
                if (i & pow(2,j)):
                    array[j]=1
                    cost=cost+a[j]
            for j in b:
                if 0 in array[j[0]-1:j[1]]:
                    continue            
                else:
                    cost=cost+j[2]
            ans.append(cost)
        ans.sort(reverse=True)

    else:
        array=[0]*n
        cost=0
        for i in range(len(a)):
            if a[i]>0:
                array[i]=1
        for i in range(n):
            if (array[i]):
                cost=cost+a[i]
        for j in b:
            if 0 in array[j[0]-1:j[1]]:
                continue            
            else:
                mn=min(a[j[0]-1:j[1]])
                if j[2]>mn:
                    cost=cost-mn
                else:
                    cost=cost+j[2]
        ans.append(cost)
    print(' '.join(map(str,ans[0:k])))