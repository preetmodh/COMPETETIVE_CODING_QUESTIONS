for i in range(int(input())):
    n=int(input())
    a=list(map(int,input().split()))
    a.sort()
    print( (a[-1] - a[0]) + (a[-1] - a[1]) + (a[1] - a[0]) )