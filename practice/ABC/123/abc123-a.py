x = [ int( input() ) for _ in range( 5 ) ]
k = int( input() )

if max( x ) - min( x ) <= k:
    print( "Yay!" )
else:
    print( ":(" )