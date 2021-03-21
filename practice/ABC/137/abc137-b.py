K, X = map( int, input().split() )

ans = [ str( n ) for n in range( X - K + 1, X + K ) ]
print( " ".join( ans ) )