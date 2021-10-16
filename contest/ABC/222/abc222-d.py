MOD = 998244353

N = int( input() )
a = list( map( int, input().split() ) )
b = list( map( int, input().split() ) )

DP = [ [ 0 for _ in range( 3100 ) ] for _ in range( N ) ]
for j in range( a[ 0 ], b[ 0 ] + 1 ):
    DP[ 0 ][ j ] += 1
    DP[ 0 ][ j ] %= MOD

for j in range( a[ 0 ] + 1, b[ 0 ] + 1 ):
    DP[ 0 ][ j ] += DP[ 0 ][ j - 1 ]
    DP[ 0 ][ j ] %= MOD

for i in range( 1, N ):
    for j in range( a[ i ], b[ i ] + 1 ):
        DP[ i ][ j ] = DP[ i - 1 ][ min( j, b[ i - 1 ] ) ]
        DP[ i ][ j ] %= MOD
    
    for j in range( a[ i ] + 1, b[ i ] + 1 ):
        DP[ i ][ j ] += DP[ i ][ j - 1 ]
        DP[ i ][ j ] %= MOD

print( DP[ N - 1 ][ b[ -1 ] ] )