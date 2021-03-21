N = int( input() )
A, B = [], []
for _ in range( N ):
    a, b = map( int, input().split() )
    A.append( a )
    B.append( b )

ad = [ ( B[ i ] + 2 * A[ i ], i ) for i in range( N ) ]
ad.sort( reverse = True )

aoki = sum( A )
takahashi = 0

for i in range( N ):
    _, town = ad[ i ]
    takahashi += A[ town ] + B[ town ]
    aoki -= A[ town ]
    # print( "town:", town, aoki, takahashi )
    if takahashi > aoki:
        print( i + 1 )
        break