n=int(input())
if(n==0):
    print('1')
else:
    print(int((3**(n-1))%(10**6 + 3)))