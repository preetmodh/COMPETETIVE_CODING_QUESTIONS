def calculate(p, q): 
     
    mod = 998244353
    expo = 0
    expo = mod - 2
 
    while (expo): 
        if (expo & 1): 
            p = (p * q) % mod 
        q = (q * q) % mod 
 
        expo >>= 1
 
    return p 

print(calculate(4,6))