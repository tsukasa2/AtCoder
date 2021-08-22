# factize( 252 ) -> [ ( 2, 2 ), ( 3, 2 ), ( 7, 1 ) ]
def factorize( n ):
    res = []
    tmp = n
    r = 0
    if tmp % 2 == 0:
        while tmp % 2 == 0:
            tmp //= 2
            r += 1
        
        res.append( ( 2, r ) )
    
    p = 3
    while p <= n ** 0.5 + 1:
        if tmp % p != 0:
            p += 2
            continue

        r = 0
        while tmp % p == 0:
            tmp //= p
            r += 1

        res.append( ( p, r ) )
        p += 2
    
    if tmp != 1:
        res.append( ( tmp, 1 ) )
    
    if len( res ) == 0 and n > 1:
        res = [ ( n, 1 ) ]

    return res

print( factorize( 252 ) )