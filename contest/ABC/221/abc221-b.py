S = str( input() )
T = str( input() )

diff_S = []
diff_T = []
diff = []
for i in range( len( S ) ):
    if not S[ i ] == T[ i ]:
        diff_S.append( S[ i ] )
        diff_T.append( T[ i ] )
        diff.append( i )

diff_S.sort()
diff_T.sort()

if len( diff ) == 0:
    print( "Yes" )
elif len( diff ) == 2 and diff_S == diff_T:
    if diff[ 0 ] + 1 == diff[ 1 ]:
        print( "Yes" )
    else:
        print( "No" )
else:
    print( "No" )