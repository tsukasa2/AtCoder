a, b = map( str, input().split( "." ) )

if int( b[ 0 ] ) < 5:
    print( a )
else:
    print( int( a ) + 1 )