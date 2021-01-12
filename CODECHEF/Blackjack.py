def checkSum(a,x,y):
    sum=0
    for i in range(len(a)):
        sum=sum+a[i]
        if sum>=x and sum<=y:
            return True
        if sum>y:
            return False
    return False

def calculate(a,ind,x,y):

    if checkSum(a,x,y):
        return 0


    for i in range(ind,len(a)):
        for j in range(0,len(a)):
            a[i],a[j]=a[j],a[i]
            if checkSum(a,x,y):
                return 1
            else:
                a[i],a[j]=a[j],a[i]

    s=set({a[0]})
    for i in range(1,len(a)):
        for j in list(s):
            s.add(a[i])
            sum1=j + a[i]
            s.add(sum1)
            if (sum1)>=x and sum1<=y:
                return 2

    return -1





for _ in range(int(input())):
    n,x,y=map(int,input().split())
    a=list(map(int,input().split()))
    sum=0
    ind=0
    for i in range(len(a)):
        sum=sum+a[i]
        if sum>y:
            ind=i
            break
        if a[i]>y:
            ind=i
            break
    
    print(calculate(a,ind,x,y))
    


    
