import math

def get_sieve_of_eratosthenes(n):
    if not isinstance(n, int):
        raise TypeError('n is int type.')
    if n < 2:
        raise ValueError('n is more than 2')
    prime = []
    limit = math.sqrt(n)
    data = [i + 1 for i in range(1, n)]
    while True:
        p = data[0]
        if limit <= p:
            return prime + data
        prime.append(p)
        data = [e for e in data if e % p != 0]

primes = get_sieve_of_eratosthenes( 2 * 10 ** 5 + 100 )

MOD = 998244353

# factorize( 18 ) = [ ( 2, 1 ), ( 3, 2 ) ]
def factorize( n ):
    res = []
    i = 0
    p = primes[ i ]
    tmp = n
    while p <= n ** 0.5 + 1:
        if tmp % p != 0:
            i += 1
            p = primes[ i ]
            continue
        r = 0
        while tmp % p == 0:
            tmp //= p
            r += 1
        res.append( ( p, r ) )
        i += 1
        p = primes[ i ]
    
    if tmp != 1:
        res.append( ( tmp, 1 ) )
    
    if len( res ) == 0 and n > 1:
        res = [ ( n, 1 ) ]

    return res

inv = [ 1, 1 ]
fact = [ 1, 1 ]
inv_fact = [ 1, 1 ]
for k in range( 2, 3 * 10 ** 5 + 1 ):
    inv_k = ( -inv[ MOD % k ] * ( MOD // k ) ) % MOD
    inv.append( inv_k )
    fact.append( fact[ -1 ] * k % MOD )
    inv_fact.append( inv_fact[ -1 ] * inv[ k ] % MOD )

def comb( x, y ):
    return fact[ x ] * inv_fact[ y ] * inv_fact[ x - y ] % MOD

#### MAIN
N, M = map( int, input().split() )

ans = 0
for i in range( 1, M + 1 ):
    f = factorize( i )

    r = 1
    for ( p, q ) in f:
        r *= comb( q + N - 1, q )
        r %= MOD

    ans += r
    ans %= MOD

print( ans )