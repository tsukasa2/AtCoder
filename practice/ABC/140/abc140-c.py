N = int( input() )
B = list( map( int, input().split() ) )

A = [ B[ 0 ] ]
for i in range( 1, N - 1 ):
    A_i = min( B[ i - 1 ], B[ i ] )
    A.append( A_i )

A.append( B[ -1 ] )

print( sum( A ) )