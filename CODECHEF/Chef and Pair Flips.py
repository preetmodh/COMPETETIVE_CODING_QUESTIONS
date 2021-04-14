for _ in range(int(input())):
    n,m,e=map(int,input().split())
    a=[]
    b=[]
    ones=0
    for i in range(n):
        temp=list(input())
        temp=list(map(int,temp))
        ones+=temp.count(1)
        a.append(temp)
    for i in range(n):
        b.append(list(input()))
    if ones%2!=0:
        print(-1)
        continue
    k=ones//2
    if e==0:
        print(k)
    else:
        r=[]
        c=[]
        for i in range(n):
            flag=1
            cnt=0
            j1=-1
            j2=-1
            for j in range(m):
                if flag==0:
                    cnt=0
                if a[i][j]==1:
                    flag=1
                    if cnt==1:
                        cnt+=1
                        j2=j
                    if cnt==0:
                        cnt+=1
                        j1=j
                    
                if cnt==2:
                    flag=0
                if j1!=-1 and j2!=-1:
                    a[i][j1],a[i][j2]=0,0
                    r.append(('R',i+1,j1+1,j2+1))
                    j1=-1
                    j2=-1

        for j in range(m):
            flag=1
            cnt=0
            i1=-1
            i2=-1
            for i in range(n):
                if flag==0:
                    cnt=0
                if a[i][j]==1:
                    flag=1
                    if cnt==1:
                        cnt+=1
                        i2=i
                    if cnt==0:
                        cnt+=1
                        i1=i
                    
                if cnt==2:
                    flag=0
                if i1!=-1 and i2!=-1:
                    a[i1][j],a[i2][j]=0,0
                    r.append(('C',j+1,i1+1,i2+1))
                    i1=-1
                    i2=-1

        print(k)
        for i in r:
            print(*i)
        for j in c:
            print(*j)
        print(a)


