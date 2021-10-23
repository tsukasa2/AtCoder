X, Y, A, B, C = map( int, input().split() )

for _ in range( 3 ):
    # Aと（B＋C）の境界が縦
    s, t = X - ( A + Y - 1 ) // Y, Y

    if s * t > 0:
        if ( B + s - 1 ) // s + ( C + s - 1 ) // s <= t:
            print( "Yes" )
            break
        elif ( B + t - 1 ) // t + ( C + t - 1 ) // t <= s:
            print( "Yes" )
            break
    
    # Aと（B＋C）の境界が横
    s, t = Y - ( A + X - 1 ) // X, X

    if s * t > 0:
        if ( B + s - 1 ) // s + ( C + s - 1 ) // s <= t:
            print( "Yes" )
            break
        elif ( B + t - 1 ) // t + ( C + t - 1 ) // t <= s:
            print( "Yes" )
            break
    
    A, B, C = B, C, A

else:
    print( "No" )