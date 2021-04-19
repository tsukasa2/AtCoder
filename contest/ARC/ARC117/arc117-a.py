A, B = map( int, input().split() )

if A > B:
    E = [ i + 1 for i in range( A ) ]
    sum_A = ( 1 + A ) * A // 2
    for b in range( B - 1 ):
        E.append( -b - 1 )
    sum_B = ( 1 + ( B - 1 ) ) * ( B - 1 ) // 2
    E.append( -( sum_A - sum_B ) )
else:
    E = [ -i - 1 for i in range( B ) ]
    sum_B = ( 1 + B ) * B // 2
    for a in range( A - 1 ):
        E.append( a + 1 )
    sum_A = ( 1 + ( A - 1 ) ) * ( A - 1 ) // 2
    E.append( sum_B - sum_A )

print( *E, sep=" " )