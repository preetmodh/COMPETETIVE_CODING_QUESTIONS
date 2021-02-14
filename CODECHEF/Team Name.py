import sys
for i in range(int(input())):
    n=int(input())
    a=set((sys.stdin.readline()).split())
    bset=[]
    s=set()
    cnt=0
    for i in a:
        s.add(i[0])
    for i in a:
        for j in s:
            if (j + i[1:]) not in a:
                bset.append(j + i[1:])
    bset=list(set(bset))
    for i in range(len(bset)):
        for j in range(i+1,len(bset)):
            #itemp = bset[j][0] + bset[i][1:]
            #jtemp = bset[i][0] + bset[j][1:]
            if ((bset[j][0] + bset[i][1:]) in a) and ((bset[i][0] + bset[j][1:]) in a):
                cnt+=2
            else:
                continue
    sys.stdout.write(str(cnt)+'\n') 
