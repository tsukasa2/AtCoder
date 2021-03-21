r_1, c_1 = map( int, input().split() )
r_2, c_2 = map( int, input().split() )

if r_1 == r_2 and c_1 == c_2:
    print( 0 )
elif r_1 + c_1 == r_2 + c_2:
    print( 1 )
elif r_1 - c_1 == r_2 - c_2:
    print( 1 )
elif abs( r_2 - r_1 ) + abs( c_2 - c_1 ) <= 3:
    print( 1 )
elif abs( ( c_1 + abs( r_2 - r_1 ) ) - c_2 ) <= 3:
    print( 2 )
elif abs( ( c_1 - abs( r_2 - r_1 ) ) - c_2 ) <= 3:
    print( 2 )
elif r_1 == r_2 and ( c_2 - c_1 ) % 2 == 0:
    print( 2 )
elif c_1 == c_2 and ( r_2 - r_1 ) % 2 == 0:
    print( 2 )
elif ( c_2 - ( c_1 + abs( r_2 - r_1 ) ) ) % 2 == 0:
    print( 2 )
elif ( c_2 - ( c_1 - abs( r_2 - r_1 ) ) ) % 2 == 0:
    print( 2 )
else:
    print( 3 )