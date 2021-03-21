A, B = map( int, input().split() )

def S( x ):
    return x // 100 + ( x % 100 ) // 10 + x % 10

print( max( S( A ), S( B ) ) )