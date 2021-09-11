S = str( input() )

y, m, d = S.split( "/" )
if int( m ) <= 4:
    print( "Heisei" )
else:
    print( "TBD" )