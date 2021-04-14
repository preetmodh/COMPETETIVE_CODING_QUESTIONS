def intersection(lst1, lst2):
    l=list(set(lst1) & set(lst2)) 
    return l

def count(i,j,p):
    ci=i.index(p)
    ri=j.index(p)
    cup=ci + 1
    cdown=len(i) - ci
    rright=len(j) - ri
    rleft=ri + 1

    cnt=0
    if cup>1 and rright>1:
        for i in range(2,min(cup,rright)+1):
            if 2*i<=max(cup,rright):
                cnt+=1
            else:
                break
        for i in range(2,max(cup,rright)+1):
            if 2*i<=min(cup,rright):
                cnt+=1
            else:
                break
    
    if cup>1 and rleft>1:
        for i in range(2,min(cup,rleft)+1):
            if 2*i<=max(cup,rleft):
                cnt+=1
            else:
                break
        for i in range(2,max(cup,rleft)+1):
            if 2*i<=min(cup,rleft):
                cnt+=1
            else:
                break
    if cdown>1 and rright>1:
        for i in range(2,min(cdown,rright)+1):
            if 2*i<=max(cdown,rright):
                cnt+=1
            else:
                break
        for i in range(2,max(cdown,rright)+1):
            if 2*i<=min(cdown,rright):
                cnt+=1
            else:
                break
    if cdown>1 and rleft>1:
        for i in range(2,min(cdown,rleft)+1):
            if 2*i<=max(cdown,rleft):
                cnt+=1
            else:
                break
        for i in range(2,max(cdown,rleft)+1):
            if 2*i<=min(cdown,rleft):
                cnt+=1
            else:
                break
    return cnt
        

for t in range(int(input())):
    r,c=map(int,input().split())
    a=[]
    for i in range(r):
        a.append(list(map(int,input().split())))
    rows=[]
    cols=[]
    for i in range(r):
        temp=[]
        for j in range(c):
            if a[i][j]==1:
                temp.append((i+1,j+1))
        for k in range(len(temp)-1):
            if (temp[k][1]+1)!=temp[k+1][1]:
                temp=[]
                break
        if len(temp)<=1:
            continue
        rows.append(temp)
    for i in range(c):
        temp=[]
        for j in range(r):
            if a[j][i]==1:
                temp.append((j+1,i+1))
        for k in range(len(temp)-1):
            if (temp[k][0]+1)!=temp[k+1][0]:
                temp=[]
                break
        if len(temp)<=1:
            continue
        cols.append(temp)
    cnt=0
    for i in cols:
        for j in rows:
            x=intersection(i, j)
            p=()
            for c in x:
                p=c
            if len(p)==0:
                continue
            cnt+=count(i,j,p)
    print("Case #"+str(t+1)+": "+str(abs(cnt)))
