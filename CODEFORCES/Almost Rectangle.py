for i in range(int(input())):
    n=int(input())
    a=[]
    I=[]
    for i in range(n):
        temp=list(input())
        if '*' in temp:
            I.append(temp.index('*'))
        a.append(temp)
    for i in range(len(a)):
        if '*' in a[i]:
            if len(I)==1:
                if i==0:
                    a[(n-1)]=a[i]
                else:
                    a[0]=a[i]
                break
                
            if I[0]==I[1]:
                if I[0]!=(n-1):
                    I[0]=(n-1)
                else:
                    I[0]=0
            a[i][I[1]]='*'
            a[i][I[0]]='*'
    for i in a:
        print(''.join(map(str,i)))
