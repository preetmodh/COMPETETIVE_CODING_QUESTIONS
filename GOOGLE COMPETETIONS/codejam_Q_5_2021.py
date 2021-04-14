t=int(input())
p=int(input())
for t in range(t):
    a=[]
    for i in range(1,100+1):
        temp=input()
        ones=temp.count('1')
        a.append((ones,i))
    a.sort()
    ans=a[-1][1]
    print("Case #"+str(t+1)+": "+str(abs(ans)))