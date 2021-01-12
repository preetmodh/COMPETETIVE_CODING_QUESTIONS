import math
import numpy
import itertools
def divisors(n):
    a=[]
    i=1
    while(i<=math.sqrt(n)):
        if (n%i)==0:
            if (n/i)==i:
                a.append(i)
            else:
                a.append(i)
                a.append(int(n/i))
        i+=1

    return sorted(a)
def phi(n) : 

	result = n 
	p = 2
	while p * p<= n : 

		if n % p == 0 : 

			while n % p == 0 : 
				n = n // p 
			result = result * (1.0 - (1.0 / float(p))) 
		p = p + 1
		
	if n > 1 : 
		result = result * (1.0 - (1.0 / float(n))) 

	return int(result)

def checkPrimitive(n):
    p=phi(n)
    a=divisors(p)
    alast=a.pop(-1)
    s=set()
    for i in range(2,n):
        if math.gcd(i,n)==1:
            for po in a:
                if pow(i,po)%n==1:
                    s.add(i)
                    break
    for i in range(2,n):
        if i not in s:
            if math.gcd(i,n)==1:
                if pow(i,alast)%n==1:
                    return True
    return False






for _ in range(int(input())):
    l,r,a,b=map(int,input().split())
    s=set(range(l,r+1))
    mul=1
    sum=0
    sub=[]
    for i in range(a,b+1):
        if i <=len(s):
            sub.append(list(itertools.combinations(s, i)))
    sum=0
    for i in range(len(sub)):
        for j in range(len(sub[i])):
            sub[i][j]=numpy.prod(list(sub[i][j]))
            sub[i][j]=divisors(sub[i][j])
    s=set({1,2,3,4})
    for i in sub:
        for j in i:
            for k in j:
                if k in s:
                    sum+=1
                elif checkPrimitive(k):
                    sum+=1
    print(sum%998244353)

            
    
    
    
