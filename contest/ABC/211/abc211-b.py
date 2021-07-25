S = [ str( input() ) for _ in range( 4 ) ]

if set( S ) == set( [ "H", "2B", "3B", "HR" ] ):
    print( "Yes" )
else:
    print( "No" )
