def maxDiff(arr, arr_size): 
    if arr_size<=1:
        return 1
    max_diff = arr[1] - arr[0] 
    min_element = arr[0] 
      
    for i in range( 0, arr_size ): 
        if (arr[i] - min_element > max_diff): 
            max_diff = arr[i] - min_element 
      
        if (arr[i] < min_element): 
            min_element = arr[i] 
    if max_diff<=0:
        max_diff=0
    return max_diff + 1

n,q,s=map(int,input().split())
a=list(map(int,input().split()))
c=[]
for i in range(0,len(a)):
    mx=a[i]
    cnt=1
    for j in range(i+1,len(a)):
        if a[j]>mx:
            mx=a[j]
            cnt+=1
        else:
            continue
    c.append(cnt)
Lans=0
for queries in range(q):
    x,y=map(int,input().split())
    l=(x + s*Lans -1) % n
    r=(y + s*Lans -1) % n
    if l>r:
        l,r=r,l
    temp=c[l:r+1]
    temp.reverse()
    Lans=maxDiff(temp,len(temp))

    print(Lans)