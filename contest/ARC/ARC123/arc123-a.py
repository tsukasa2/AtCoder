A = list( map( int, input().split() ) )

if A[ 1 ] < ( A[ 0 ] + A[ 2 ] ) / 2:
    if ( A[ 0 ] + A[ 2 ] ) % 2 == 0:
        print( ( A[ 0 ] + A[ 2 ] ) // 2 - A[ 1 ] )
    else:
        print( ( A[ 0 ] + A[ 2 ] + 1 ) // 2 - A[ 1 ] + 1 )
else:
    print( abs( ( A[ 2 ] - A[ 1 ] ) - ( A[ 1 ] - A[ 0 ] ) ) )