N, Q = map( int, input().split() )
query = [ tuple( map( int, input().split() ) ) for _ in range( Q ) ]

link = [ [ -1, -1 ] for _ in range( N ) ]
for q in query:
    if q[ 0 ] == 1:
        x, y = q[ 1 ] - 1, q[ 2 ] - 1
        link[ x ][ 1 ] = y
        link[ y ][ 0 ] = x
    elif q[ 0 ] == 2:
        x, y = q[ 1 ] - 1, q[ 2 ] - 1
        link[ x ][ 1 ] = -1
        link[ y ][ 0 ] = -1
    else:
        x = q[ 1 ] - 1
        while not link[ x ][ 0 ] == -1:
            x = link[ x ][ 0 ]
        
        j = []
        while not x == -1:
            j.append( x + 1 )
            x = link[ x ][ 1 ]

        print( len( j ), " ".join( map( str, j ) ) )
