N = int( input() )
A = list( map( int, input().split() ) )
B = list( map( int, input().split() ) )

naiseki = 0
for i in range( N ):
    naiseki += A[ i ] * B[ i ]

if naiseki == 0:
    print( "Yes" )
else:
    print( "No" )