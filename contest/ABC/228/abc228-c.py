N, K = map( int, input().split() )
P = [ list( map( int, input().split() ) ) for _ in range( N ) ]

order = [ ( sum( P[ i ] ), i ) for i in range( N ) ]
order.sort( reverse = True )

limit = order[ K - 1 ][ 0 ]
for ( p_0, p_1, p_2 ) in P:
    if p_0 + p_1 + p_2 + 300 >= limit:
        print( "Yes" )
    else:
        print( "No" )
