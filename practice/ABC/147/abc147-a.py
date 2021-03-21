A_1, A_2, A_3 = map( int, input().split() )

if A_1 + A_2 + A_3 > 21:
    print( "bust" )
else:
    print( "win" )