N = int( input() )
A = list( map( int, input().split() ) )

def solve( array, i=0, xored=0, ored=0 ):
    if len( array ) - 1 == i:
        return xored ^ ( ored | array[ -1 ] )
    else:
        return min( solve( array, i + 1, xored ^ ( ored | array[ i ] ), 0 ),
            solve( array, i + 1, xored, ored | array[ i ] ) )

print( solve( A ) )