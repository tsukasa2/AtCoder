N, M, X, Y = map( int, input().split() )
x = list( map( int, input().split() ) )
y = list( map( int, input().split() ) )

x_max = max( x + [ X ] )
y_min = min( y + [ Y ] )
if x_max < y_min:
    print( "No War" )
else:
    print( "War" )