N, M = map( int, input().split() )
B = [ tuple( map( int, input().split() ) ) for _ in range( N ) ]

for i in range( N ):
    for j in range( M - 1 ):
        if B[ i ][ j ] + 1 == B[ i ][ j + 1 ]:
            if ( B[ i ][ j ] - 1 ) % 7 + 1 == ( B[ i ][ j + 1 ] - 1 ) % 7:
                continue
    
        print( "No" )
        exit()

for i in range( N - 1 ):
    for j in range( M ):
        if B[ i ][ j ] + 7 == B[ i + 1 ][ j ]:
            continue
        
        print( "No" )
        exit()

print( "Yes" )