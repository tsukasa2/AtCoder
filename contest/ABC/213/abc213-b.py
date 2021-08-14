N = int( input() )
A = list( map( int, input().split() ) )

A_ID = [ ( a, i + 1 ) for i, a in enumerate( A ) ]

A_ID.sort()
print( A_ID[ -2 ][ 1 ] )