N = int( input() )
L = list( map( int, input().split() ) )

L_max = max( L )
L_sum = sum( L )
if L_max < L_sum - L_max:
    print( "Yes" )
else:
    print( "No" )