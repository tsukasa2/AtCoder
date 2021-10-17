N = int( input() )
T, A = map( int, input().split() )
H = list( map( int, input().split() ) )

lis = []
for i, h in enumerate( H ):
    d = abs( ( T - 0.006 * h ) - A )
    lis.append( ( d, i + 1 ) )

lis.sort()
print( lis[ 0 ][ 1 ] )