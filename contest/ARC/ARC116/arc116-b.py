MOD = 998244353

N = int( input() )
A = list( map( int, input().split() ) )

A.sort()

s = []
for i in reversed( range( N ) ):
    s.append( A[ i ] * pow( 2, i, MOD ) % MOD )

for i in range( 1, N ):
    s[ i ] += s[ i - 1 ]
    s[ i ] %= MOD
s = [ 0 ] + s

ans = 0
for i in range( N ):
    ans += ( s[ -i - 1 ] + A[ i ] * pow( 2, i, MOD ) ) * A[ i ] * pow( 2, -( i + 1 ), MOD )
    ans %= MOD

print( ans )