A, B = map( int, input().split() )

# factorize( 18 ) = [ ( 2, 1 ), ( 3, 2 ) ]
def factorize( n ):
    res = []
    p = 2
    tmp = n
    while p <= n ** 0.5 + 1:
        if tmp % p != 0:
            p += 1
            continue
        r = 0
        while tmp % p == 0:
            tmp //= p
            r += 1
        res.append( ( p, r ) )
        p += 1
    
    if tmp != 1:
        res.append( ( tmp, 1 ) )
    
    if len( res ) == 0 and n > 1:
        res = [ ( n, 1 ) ]

    return res

import math

g = math.gcd( A, B )

print( 1 + len( factorize( g ) ) )
