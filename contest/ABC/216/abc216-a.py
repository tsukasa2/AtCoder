X, Y = map( str, input().split( "." ) )

if int( Y ) <= 2:
    print( X + "-" )
elif int( Y ) <= 6:
    print( X )
else:
    print( X + "+" )