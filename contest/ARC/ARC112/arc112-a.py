T = int( input() )
case = [ tuple( map( int, input().split() ) ) for _ in range( T ) ]

for ( L, R ) in case:
    if R - L < L:
        print( 0 )
    else:
        print( ( R - 2 * L + 1 ) * ( R - 2 * L + 2 ) // 2 )