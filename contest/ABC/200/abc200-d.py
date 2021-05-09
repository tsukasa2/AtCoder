from itertools import chain, combinations
def powerset( iterable ):
    # powerset( [ 1, 2, 3 ] )
    # --> () ( 1, ) ( 2, ) ( 3, ) ( 1, 2 ) ( 1, 3 ) ( 2, 3 ) ( 1, 2, 3 )
    s = list( iterable )
    return chain.from_iterable( combinations( s, r ) for r in range( len( s ) + 1 ) )

N = min( 8, int( input() ) )
A = list( map( int, input().split() ) )

for i in range( N ):
    A[ i ] = A[ i ] % 200

BC = [ [] for _ in range( 200 ) ]
# BC[ i ] = 和を200で割った余りがiになる数列
for p in powerset( range( N ) ):
    sum_p = 0
    for i in p:
        sum_p += A[ i ]
        sum_p %= 200

    if len( BC[ sum_p ] ) > 0:
        print( "Yes" )
        print( len( BC[ sum_p ] ), " ".join( map( str, BC[ sum_p ] ) ) )
        print( len( p ), " ".join( map( str, [ i + 1 for i in p ] ) ) )
        break
    else:
        for i in p:
            BC[ sum_p ].append( i + 1 )
else:
    print( "No" )