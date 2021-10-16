N, M = map( int, input().split() )
A = [ str( input() ) for _ in range( 2 * N ) ]

players = [ ( 0, i ) for i in range( 2 * N ) ]
for i in range( M ):
    for j in range( N ):
        w_a, p_a = players[ 2 * j ]
        w_b, p_b = players[ 2 * j + 1 ]

        x, y = A[ p_a ][ i ], A[ p_b ][ i ]
        if x == y:
            continue
        elif ( x, y ) == ( "G", "C" ):
            players[ 2 * j ] = ( w_a - 1, p_a )
        elif ( x, y ) == ( "C", "P" ):
            players[ 2 * j ] = ( w_a - 1, p_a )
        elif ( x, y ) == ( "P", "G" ):
            players[ 2 * j ] = ( w_a - 1, p_a )
        else:
            players[ 2 * j + 1 ] = ( w_b - 1, p_b )
    
    players.sort()

for _, p in players:
    print( p + 1 )