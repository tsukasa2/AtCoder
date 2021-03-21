MOD = 10 ** 9 + 7
S = str( input() )

L = len( S )
DP = [ [ 0 for _ in range( 13 ) ] for _ in range( L + 1 ) ]
DP[ 0 ][ 0 ] = 1

for i in range( L ):
    for j in range( 13 ):
        k = S[ i ]
        if k == "?":
            for l in range( 10 ):
                DP[ i + 1 ][ ( 10 * j + l ) % 13 ] += DP[ i ][ j ]
                DP[ i + 1 ][ ( 10 * j + l ) % 13 ] %= MOD
        else:
            DP[ i + 1 ][ ( 10 * j + int( k ) ) % 13 ] += DP[ i ][ j ]
            DP[ i + 1 ][ ( 10 * j + int( k ) ) % 13 ] %= MOD

print( DP[ L ][ 5 ] )