N = int( input() )
S = [ str( input() ) for _ in range( N ) ]

dp = [ 0 for _ in range( N + 1 ) ]
dp[ 0 ] = 1
for i in range( N ):
    if S[ i ] == "AND":
        dp[ i + 1 ] = dp[ i ]
    elif S[ i ] == "OR":
        dp[ i + 1 ] = pow( 2, i + 1 ) + dp[ i ]

print( dp[ N ] )