N = int( input() )
S = str( input() )

DP = [ [ 0 ] * N for _ in range( N ) ]
for i in range( N ):
    if S[ i ] == S[ N - 1 ]:
        DP[ i ][ N - 1 ] = 1
        DP[ N - 1 ][ i ] = 1

for i in reversed( range( N - 1 ) ):
    for j in reversed( range( N - 1 ) ):
        if S[ i ] == S[ j ]:
            DP[ i ][ j ] = DP[ i + 1 ][ j + 1 ] + 1

for i in range( N ):
    print( sum( DP[ i ] ) )