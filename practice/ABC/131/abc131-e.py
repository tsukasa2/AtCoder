import itertools

N, K = map( int, input().split() )

if ( N - 1 ) * ( N - 2 ) // 2 < K:
    print( -1 )
else:
    M = N - 1
    edge = [ ( 1, i ) for i in range( 2, N + 1 ) ]
    to_connect = ( N - 1 ) * ( N - 2 ) // 2 - K
    for c in itertools.combinations( list( range( 2, N + 1 ) ), 2 ):
        if to_connect == 0:
            break
        edge.append( tuple( c ) )
        M += 1
        to_connect -= 1
    
    print( M )
    for e in edge:
        print( " ".join( map( str, e ) ) )
