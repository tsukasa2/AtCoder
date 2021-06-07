x, y = map( int, input().split() )

if x == y:
    print( x )
elif set( [ x, y ] ) == set( [ 0, 1 ] ):
    print( 2 )
elif set( [ x, y ] ) == set( [ 1, 2 ] ):
    print( 0 )
else:
    print( 1 )