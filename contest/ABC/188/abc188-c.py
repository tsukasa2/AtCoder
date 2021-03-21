N = int( input() )
A = list( map( int, input().split() ) )

max_A = max( A )
first = A.index( max_A )

if first >= pow( 2, N - 1 ):
    second_max_A = max( A[ : pow( 2, N - 1 ) ] )
else:
    second_max_A = max( A[ pow( 2, N - 1 ) : ] )

print( A.index( second_max_A ) + 1 )