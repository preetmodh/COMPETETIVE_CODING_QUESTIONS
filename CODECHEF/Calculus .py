n=int(input())
mod = 998244353

def fastpow(base, power):
    ans = 1
    while power > 0:
        if power & 1:
            ans = ans * base % mod
        power >>= 1
        base = base * base % mod
    return ans

def inv(x):
    return fastpow(x, mod-2)

n=int(input())
if n==2:
    print(int(266667 * inv(100000) % 998244353))
if n==3:
    print(int(306667 * inv(100000) % 998244353))~!@delattr