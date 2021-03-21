n, k, m = map( int, input().split() )
a = list( map( int, input().split() ) )

a_n =  max( m * n - sum( a ), 0 )
if a_n > k:
    print( -1 )
else:
    print( a_n )