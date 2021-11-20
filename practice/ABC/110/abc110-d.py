MOD = 10 ** 9 + 7
N, M = map( int, input().split() )

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

inv = [ 1, 1 ]
fact = [ 1, 1 ]
inv_fact = [ 1, 1 ]
for k in range( 2, 2 * 10 ** 5 + 100 ):
    inv_k = ( -inv[ MOD % k ] * ( MOD // k ) ) % MOD
    inv.append( inv_k )
    fact.append( fact[ -1 ] * k % MOD )
    inv_fact.append( inv_fact[ -1 ] * inv[ k ] % MOD )

def comb( x, y ):
    return fact[ x ] * inv_fact[ y ] * inv_fact[ x - y ] % MOD

factors = factorize( M )
ans = 1
for x, y in factors:
    ans = ans * comb( N - 1 + y, y ) % MOD

print( ans )
# print( factors )