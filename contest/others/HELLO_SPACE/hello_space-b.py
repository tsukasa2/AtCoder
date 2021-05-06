N, D, H = map( int, input().split() )
DH = [ tuple( map( int, input().split() ) ) for _ in range( N ) ]

min_m = 1000000
for ( d, h ) in DH:
    m = ( H - h ) / ( D - d )
    min_m = min( min_m, m )

print( max( 0, H - min_m * D ) )