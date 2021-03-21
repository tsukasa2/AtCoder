K = int( input() )

def factorize( n ):
    res = 1
    p = 2
    tmp = n
    r = 0
    while tmp % p == 0:
        tmp //= p
        r += 1
    res *= ( r + 2 ) * ( r + 1 ) // 2
    p += 1
    while p <= n ** 0.5 + 1:
        if tmp % p != 0:
            p += 2
            continue
        r = 0
        while tmp % p == 0:
            tmp //= p
            r += 1
        res *= ( r + 2 ) * ( r + 1 ) // 2
        p += 2
    
    if tmp != 1:
        res *= ( 1 + 2 ) * ( 1 + 1 ) // 2

    return res

ans = 0
for k in range( 1, K + 1 ):
    ans += factorize( k )

print( ans )
