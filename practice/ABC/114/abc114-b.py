S = str( input() )

ans = 1000
for i in range( len( S ) - 2 ):
    n = int( S[ i ] + S[ i + 1 ] + S[ i + 2 ] )
    ans = min( ans, abs( n - 753 ) )

print( ans )