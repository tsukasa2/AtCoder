N, M, K = map( int, input().split() )
UV = [ tuple( map( int, input().split() ) ) for _ in range( M ) ]

MOD = 998244353

DP = [ [ 0 ] * N for _ in range( K + 1 ) ]
DP[ 0 ][ 0 ] = 1

for k in range( K ):
    sum_DP_k = sum( DP[ k ] ) % MOD
    for i in range( N ):
        DP[ k + 1 ][ i ] = sum_DP_k
    
    for ( u, v ) in UV:
        u, v = u - 1, v - 1
        DP[ k + 1 ][ u ] -= DP[ k ][ v ]
        DP[ k + 1 ][ u ] %= MOD
        DP[ k + 1 ][ v ] -= DP[ k ][ u ]
        DP[ k + 1 ][ v ] %= MOD
    
    for i in range( N ):
        DP[ k + 1 ][ i ] -= DP[ k ][ i ]
        DP[ k + 1 ][ i ] %= MOD

print( DP[ K ][ 0 ] )