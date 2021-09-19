N = int( input() )
X, Y = map( int, input().split() )
AB = [ tuple( map( int, input().split() ) ) for _ in range( N ) ]

DP = [ 
    [ 
        [ 10 ** 12 ] * ( Y + 1 ) for _ in range( X + 1 ) 
    ] for _ in range( N + 1 )
]
# DP[ i ] = お弁当_0〜お弁当_iでの答え

for i in range( N ):
    DP[ i ][ 0 ][ 0 ] = 0

for i, ( a, b ) in enumerate( AB ):
    for x in range( X + 1 ):
        for y in range( Y + 1 ):
            DP[ i + 1 ][ x ][ y ] = DP[ i ][ x ][ y ]
            x2 = max( 0, x - a )
            y2 = max( 0, y - b )
            # print( i, x, y, DP[ i ][ x ][ y ], DP[ i ][ x2 ][ y2 ] )
            DP[ i + 1 ][ x ][ y ] = min(
                DP[ i + 1 ][ x ][ y ],
                DP[ i ][ x2 ][ y2 ] + 1
            )

# for dp in DP:
#     print( dp )
if DP[ N ][ X ][ Y ] >= 10 ** 12:
    print( -1 )
else:
    print( DP[ N ][ X ][ Y ] )