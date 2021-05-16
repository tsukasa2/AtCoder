H, W = map( int, input().split() )
A = [ str( input() ) for _ in range( H ) ]

D = [ [ 0 for _ in range( W ) ] for _ in range( H ) ]
for i in range( H ):
    for j in range( W ):
        if A[ i ][ j ] == "+":
            D[ i ][ j ] = +1
        else:
            D[ i ][ j ] = -1

DP = [ [ 0 for _ in range( W ) ] for _ in range( H ) ]
for i in reversed( range( H - 1 ) ):
    if ( i + ( W - 1 ) ) % 2 == 1:
        if A[ i + 1 ][ W - 1 ] == "+":
            DP[ i ][ W - 1 ] = DP[ i + 1 ][ W - 1 ] - 1
        else:
            DP[ i ][ W - 1 ] = DP[ i + 1 ][ W - 1 ] + 1
    else:
        if A[ i + 1 ][ W - 1 ] == "+":
            DP[ i ][ W - 1 ] = DP[ i + 1 ][ W - 1 ] + 1
        else:
            DP[ i ][ W - 1 ] = DP[ i + 1 ][ W - 1 ] - 1

for j in reversed( range( W - 1 ) ):
    if ( ( H - 1 ) + j ) % 2 == 1:
        if A[ H - 1 ][ j + 1 ] == "+":
            DP[ H - 1 ][ j ] = DP[ H - 1 ][ j + 1 ] - 1
        else:
            DP[ H - 1 ][ j ] = DP[ H - 1 ][ j + 1 ] + 1
    else:
        if A[ H - 1 ][ j + 1 ] == "+":
            DP[ H - 1 ][ j ] = DP[ H - 1 ][ j + 1 ] + 1
        else:
            DP[ H - 1 ][ j ] = DP[ H - 1 ][ j + 1 ] - 1

for i in reversed( range( H - 1 ) ):
    for j in reversed( range( W - 1 ) ):
        if ( i + j ) % 2 == 1:
            right = DP[ i ][ j + 1 ] - D[ i ][ j + 1 ]
            down = DP[ i + 1 ][ j ] - D[ i + 1 ][ j ]
            DP[ i ][ j ] = min( right, down )
        else:
            right = DP[ i ][ j + 1 ] + D[ i ][ j + 1 ]
            down = DP[ i + 1 ][ j ] + D[ i + 1 ][ j ]
            DP[ i ][ j ] = max( right, down )

if DP[ 0 ][ 0 ] > 0:
    print( "Takahashi" )
elif DP[ 0 ][ 0 ] == 0:
    print( "Draw" )
else:
    print( "Aoki" )