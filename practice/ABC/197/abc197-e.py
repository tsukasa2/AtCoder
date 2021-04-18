N = int( input() )
XC = [ tuple( map( int, input().split() ) ) for _ in range( N ) ]

INF = 10 ** 18

LR = [ [ INF, -INF ] for _ in range( N + 1 ) ]
for ( x, c ) in XC:
    LR[ c ][ 0 ] = min( LR[ c ][ 0 ], x )
    LR[ c ][ 1 ] = max( LR[ c ][ 1 ], x )

DP = [ [ INF, INF ] for _ in range( N + 2 ) ]
DP[ 0 ][ 0 ] = 0
DP[ 0 ][ 1 ] = 0

X = [ [ 0, 0 ] for _ in range( N + 2 ) ]

i = 0
for ( l, r ) in LR:
    i += 1
    if r == -INF:
        DP[ i ] = DP[ i - 1 ]
        X[ i ] = X[ i - 1 ]
        continue
    
    DP[ i ][ 0 ] = abs( r - l ) + min( abs( r - X[ i - 1 ][ 0 ] ) + DP[ i - 1 ][ 0 ], abs( r - X[ i - 1 ][ 1 ] ) + DP[ i - 1 ][ 1 ] )
    X[ i ][ 0 ] = l
    DP[ i ][ 1 ] = abs( r - l ) + min( abs( l - X[ i - 1 ][ 0 ] ) + DP[ i - 1 ][ 0 ], abs( l - X[ i - 1 ][ 1 ] ) + DP[ i - 1 ][ 1 ] )
    X[ i ][ 1 ] = r

# print( *LR, sep="\n" )
# print( *DP, sep="\n" )
# print( *X, sep="\n" )
print( min( DP[ -1 ][ 0 ] + abs( X[ -1 ][ 0 ] ), DP[ -1 ][ 1 ] + abs( X[ -1 ][ 1 ] ) ) )