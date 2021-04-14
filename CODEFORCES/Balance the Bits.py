for i in range(int(input())):
    n=int(input())
    s=input()
    a=''
    b=''
    for i in range(n):
        if i%2==0:
            a+='('
        else:
            a+=')'
    bo=0
    bc=0
    flag=True
    for i in range(n):
        if s[i]=='1':
            b+=a[i]
            if a[i]=='(':
                bo+=1
            else:
                bc+=1
                if bc>bo:
                    flag=False
                    break
        else:
            if a[i]=='(':
                b+=')'
                bc+=1
                if bc>bo:
                    flag=False
                    break
            else:
                b+='('
                bo+=1
    if (not flag) or (bo!=bc):
        print("NO")

    else:
        print("YES")
        print(a)
        print(b)

