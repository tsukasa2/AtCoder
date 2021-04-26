N = int( input() )
A = list( map( int, input().split() ) )
B = list( map( int, input().split() ) )

max_A = max( A )
min_B = min( B )
print( max( 0, min_B - max_A + 1 ) )