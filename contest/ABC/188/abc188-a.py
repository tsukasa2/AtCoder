X, Y = map( int, input().split() )

if X > Y:
    X, Y = Y, X

if X + 3 > Y:
    print( "Yes" )
else:
    print( "No" )