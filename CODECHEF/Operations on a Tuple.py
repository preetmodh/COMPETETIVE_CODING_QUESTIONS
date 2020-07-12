# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 12:02:13 2020

@author: PREET MODH
"""


for _ in range(int(input())):
    a=list(map(int,input().split()))
    b=list(map(int,input().split()))
    ac=a.copy()
    p=a[0]
    q=a[1]
    r=a[2]
    bc=b.copy()
    cntadd=0
    cntmul=0
    cntma=3
    cntam=3
    for i in range(len(a)):
        a[i]=(a[i]-b[i])
        if b[i]!=0:
            b[i]=(a[i]+b[i])/b[i]
        else:
            b[i]=0
    a.sort()
    b.sort()
    a.append(a[-1]+1)
    b.append(b[-1]+1)
    for i in range(len(a)-1):
        if a[i]!=a[i+1] and a[i]!=0:
            cntadd+=1
        if b[i]!=b[i+1] and b[i]!=1:
            cntmul+=1
    if cntadd==3 and cntmul==3:
        for i in range(len(a)-1):
            if ac[i]==1:
                ac[i]=bc[i]-ac[i]
            elif ac[i]!=0:
                ac[i]=bc[i]//ac[i]
        if ac.count(ac[i])==len(ac):
            cntma=2
        for i in range(1+min(bc)+1):
            if bc[0]!=0 and bc[1]!=0 and bc[2]!=0:
                p=p+i
                q=q+i
                r=r+i
                if (p/bc[0])==(q/bc[1]) or (q/bc[1])==(r/bc[2]):
                    cntam=2
                    break
                p=p-i
                q=q-i
                r=r-i
            else:
                break
    print(min(cntadd,cntmul,cntma,cntam))
        