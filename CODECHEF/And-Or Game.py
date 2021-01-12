for _ in range(int(input())):
    n,m=map(int,input().split())
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    vlist=[0]
    vset=set({0})
    for x in vlist:
        for i in a:
            if i|x not in vset:
                vset.add(i|x)
                vlist.append(i|x)
        for j in b:
            if j&x not in vset:
                vset.add(j&x)
                vlist.append(j&x)
    print(len(vset))
    #print(vset)
