N, K = map( int, input().split() )
L, R = [], []
for _ in range( K ):
    L_i, R_i = map( int, input().split() )
    L.append( L_i )
    R.append( R_i )

MOD = 998244353

DP = [ 0 for _ in range( N + 10 ) ]
DP[ 1 ] = 1
# DP[ i ] = マスiに行く方法の数 % MOD
SDP = [ 0 for _ in range( N + 10 ) ]
SDP[ 1 ] = 1
# SDP[ i ] = DP[ 1 ] + DP[ 2 ] + ... + DP[ i ]

for i in range( 2, N + 1 ):
    for j in range( K ):
        if i - L[ j ] < 1:
            continue
        r = max( 1, i - L[ j ] )
        l = max( 1, i - R[ j ] )
        DP[ i ] += SDP[ r ] - SDP[ l - 1 ]
        DP[ i ] %= MOD
    SDP[ i ] = SDP[ i - 1 ] + DP[ i ]
    SDP[ i ] %= MOD

print( DP[ N ] )