N = int( input() )

P = [ [ 0.0 for _ in range( N + 1 ) ] for _ in range( 100 ) ]

P[ 0 ][ 1 ] = 1.0

for i in range( 1, 100 ):
    for j in range( 1, N + 1 ):
        P[ i ][ j ] += P[ i - 1 ][ j ] + ( N - ( j - 1 ) ) * P[ i - 1 ][ j - 1 ] / N

for i in range( 100 ):
    print( P[ i ] )