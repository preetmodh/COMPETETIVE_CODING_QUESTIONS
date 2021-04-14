for i in range(int(input())):
    s=input()
    s=list(s)
    ans="NO"
    string=''
    if len(s)%2!=0:
        if s[len(s)//2]!='a':
            s=s[:len(s)//2+1]+['a']+s[len(s)//2+1:]
            print("YES")
            print(''.join(map(str,s)))
        else:
            ind=-1
            for i in range(len(s)):
                if s[i]!='a':
                    ind=i
                    break
            if ind!=-1:
                ind=len(s)-i
                s=s[:ind]+['a']+s[ind:]
                print("YES")
                print(''.join(map(str,s)))
            else:
                print("NO")
    else:
        ind=-1
        for i in range(len(s)):
            if s[i]!='a':
                ind=i
                break
        if ind!=-1:
            ind=len(s)-i
            s=s[:ind]+['a']+s[ind:]
            print("YES")
            print(''.join(map(str,s)))
        else:
            print("NO")

