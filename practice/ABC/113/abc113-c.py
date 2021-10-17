N, M = map( int, input().split() )
PY = [ tuple( map( int, input().split() ) ) for _ in range( M ) ]

YP = [ ( y, p, i ) for i, ( p, y ) in enumerate( PY ) ]
YP.sort()

count = [ 0 ] * N
ans = [ "" ] * M
for y, p, i in YP:
    count[ p - 1 ] += 1
    ans[ i ] = str( p ).zfill( 6 ) + str( count[ p - 1 ] ).zfill( 6 )

print( *ans, sep = "\n" )