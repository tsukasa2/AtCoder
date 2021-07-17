N, X = map( int, input().split() )
A = list( map( int, input().split() ) )

if X < sum( A ) - ( N // 2 ):
    print( "No" )
else:
    print( "Yes" )