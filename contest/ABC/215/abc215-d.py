N, M = map( int, input().split() )
A = list( map( int, input().split() ) )

# N = 100000
# M = 100000
# A = [ i for i in range( 1, 10 ** 5 + 1 ) ]

def factorize( n ):
    res = []
    tmp = n

    if tmp % 2 == 0:
        while tmp % 2 == 0:
            tmp //= 2
        
        res.append( 2 )
    
    p = 3

    while p <= n ** 0.5 + 1:
        if tmp % p != 0:
            p += 2
            continue

        while tmp % p == 0:
            tmp //= p

        res.append( p )
        p += 2
    
    if tmp != 1:
        res.append( tmp )
    
    if len( res ) == 0 and n > 1:
        res = [ n ]

    return res

divisors = set()
for a in A:
    for d in factorize( a ):
        divisors.add( d )

prime = list( divisors )
data = [ 1 ] * M
for p in prime:
    i = p - 1
    while i < M:
        data[ i ] = 0
        i += p

print( sum( data ) )
for i, d in enumerate( data ):
    if d == 1:
        print( i + 1 )