input()
s=input()
count=0
level=0
for i in range(len(s)):
    if s[i]=='U':
        level=level+1
    else:
        level=level-1
    if level==0 and s[i]=='U':
        count=count+1
print(count)
    
