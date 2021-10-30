H, W = map( int, input().split() )
A = [ list( map( int, input().split() ) ) for _ in range( H ) ]

for i_1 in range( H - 1 ):
    for i_2 in range( i_1 + 1, H ):
        for j_1 in range( W - 1 ):
            for j_2 in range( j_1 + 1, W ):
                if A[ i_1 ][ j_1 ] + A[ i_2 ][ j_2 ] > A[ i_2 ][ j_1 ] + A[ i_1 ][ j_2 ]:
                    print( "No" )
                    exit()

print( "Yes" )