for i in range(int(input())):
    a,b=map(int,input().split())
    s=list(input())
    ar=a-s.count('0')
    br=b-s.count('1')
    n=len(s)-1
    for i in range(len(s)):
        if s[i]=='?' or s[n-i]=='?':
            if (s[i]=='?' and s[n-i]!='?'):
                s[i]=s[n-i]
                if s[n-i]=='1':
                    br-=1
                else:
                    ar-=1
            elif(s[i]=='?' and s[n-i]!='?'):
                s[n-i]=s[i]
                if s[i]=='1':
                    br-=1
                else:
                    ar-=1

            else:
                if br>0:
                    s[i],s[n-i]='1','1'
                    if i==n-i:
                        br-=1
                    else:
                        br-=2
                else:
                    s[i],s[n-i]='0','0'
                    if i==n-i:
                        ar-=1
                    else:
                        ar-=2
    if  s== s[::-1] and s.count('0')==a and s.count('1')==b:
        print(''.join(s))
    else:
        print(-1)
