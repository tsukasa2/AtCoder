N = int( input() )
A = list( map( int, input().split() ) )
MOD = 10 ** 9 + 7

fibonacci = [ 1, 1, 2 ]
for _ in range( 10 ** 5 + 100 ):
    fibonacci.append( ( fibonacci[ -2 ] + fibonacci[ -1 ] ) % MOD )

plumin = [ ( 1, 0 ) ]
p, m = 1, 0
for _ in range( 10 ** 5 + 100 ):
    plumin.append( ( p + m, p ) )
    tmp = p
    p = ( p + m ) % MOD
    m = tmp

ans = 0
for i, a in enumerate( A ):
    p, m = plumin[ i ]
    x = p * fibonacci[ N - i ] % MOD
    y = m * fibonacci[ N - 1 - i ] % MOD
    ans += a * ( x - y ) % MOD
    ans %= MOD

print( ans )