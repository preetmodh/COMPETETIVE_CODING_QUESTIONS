t,q,d=map(int,input().split())
for i in range(t):
    start=-(pow(10, 18)+1)
    end=pow(10, 18)+1
    y1=start
    y2=end
    c=1
    mid = (start+end)//2
    while(True):
        if start<=end:
            mid=(start+end)//2
            if c==1:
                print(c,mid,y1,flush=True)
            else:
                print(c,mid,y1,mid,y2,flush=True)
            s=input()
            if s[0]=='X':
                c=2
            if s=='O':
                break
            if s[0]=='N':
                start=mid+1
            if s[0]=='P':
                end=mid-1
        
        else:
            if c==1:
                print(c,mid,y1,flush=True)
            else:
                print(c,mid,y1,mid+d,y2,flush=True)
            s=input()
            if s[0]=='X':
                c=2
            if s=='O':
                break
            if s[0]=='N':
                mid=mid-1
            if s[0]=='P':
                mid=mid+1
            
            
