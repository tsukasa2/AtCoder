B, C = map( int, input().split() )

if C == 1:
    if B == 0:
        print( 1 )
    else:
        print( 2 )
else:
    if B > 0:
        Y = B - C // 2
        Y = max( 0, Y )
        X = - ( B - ( C - 1 ) // 2 )
        X = min( -1, X )
        W = -B - ( C - 1 ) // 2
        Z = - ( -B - ( C - 2 ) // 2 )
    else:
        W = B - C // 2
        Z = - ( B - ( C - 1 ) // 2 )
        Y = -B - ( C - 1 ) // 2
        Y = max( 0, Y )
        X = - ( -B - ( C - 2 ) // 2 )
        X = min( -1, X )

    print( ( Z - Y + 1 ) + ( X - W + 1 ) )