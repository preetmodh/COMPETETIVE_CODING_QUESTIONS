def GroupString(s):
    sub = [s[i: j] for i in range(len(s)) for j in range(i + 1, len(s) + 1)]

    d={}
    for word in sub:
        d.setdefault(len(word), []).append(word)
    result=[d[n] for n in sorted(d, reverse=True)]
    for i in range(len(result)):
        result[i]=list(set(result[i]))

    return result

def StripAndCal(c1,c2):
    s1=c1
    s2=c2
    if s1.count('1')!=s2.count('1') or (s1.count('1')==1 or s2.count('1')==1):
        return False
    else:
        I=0
        while(True):
            flag=0
            for x in range(len(s1)):
                if s1[x]!=s2[x]:
                    flag=1
                    I=x
                    break
            i,j,J=I,I,I
            cnt=0
            if s1[i]=='0':
                while(i<len(s1)):
                    if s1[i]=='1':
                        cnt+=1
                    if cnt==2:
                        J=i
                        break
                    i+=1
                if cnt==2:
                    s1=s1[0:I] + (''.join(map(str,reversed(s1[I:J+1])))) + s1[J+1:len(s1)]
                else:
                    return False
            cnt=0
            if s2[j]=='0':
                while(j<len(s2)):
                    if s2[j]=='1':
                        cnt+=1
                    if cnt==2:
                        J=j
                        break
                    j+=1
                if cnt==2:
                    s2=s2[0:I] + (''.join(map(str,reversed(s2[I:J+1])))) + s2[J+1:len(s2)]
                else:
                    return False
            if s1==s2:
                return True


for _ in range(int(input())):
    s=input()
    cnt=0
    r=GroupString(s)
    #print(r)
    for i in range(len(r)):
        if len(r[i][0])==len(s) or len(r[i][0])==1 or len(r[i][0])==2 or len(r[i])==1:
            cnt+=len(r[i])
        else:
            for j in range(len(r[i])):
                for k in range(j+1,len(r[i])):
                    if r[i][k]==-1 or r[i][j]==-1:
                        continue
                    else:
                        if StripAndCal(r[i][j],r[i][k]):
                            r[i][k]=-1
                            
            for k in range(len(r[i])):
                if r[i][k]!=-1:
                    cnt+=1
    print(cnt)



