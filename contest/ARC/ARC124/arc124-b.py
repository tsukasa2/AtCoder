N = int( input() )
a = list( map( int, input().split() ) )
b = list( map( int, input().split() ) )

digits_a = [ 0 for _ in range( 30 ) ]
digits_b = [ 0 for _ in range( 30 ) ]

for a_i in a:
    for i in range( 30 ):
        digits_a[ i ] += a_i % 2
        print( a_i % 2, end = "" )
        a_i //= 2
    print()

print( digits_a )

for b_i in b:
    for i in range( 30 ):
        digits_b[ i ] += b_i % 2
        print( b_i % 2, end = "" )
        b_i //= 2
    print()

print( digits_b )

K = int( input() )
S = [ int( input() ) for _ in range( K ) ]

for s in S:
    print( bin( s )[ ::-1 ] )