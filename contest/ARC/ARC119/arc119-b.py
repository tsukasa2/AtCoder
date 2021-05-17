N = int( input() )
S = str( input() )
T = str( input() )

while S[ N - 1 ] == T[ N - 1 ] and N > 1:
    N -= 1

if S[ : N ].count( "0" ) != T[ : N ].count( "0" ):
    print( -1 )
else:
    zeroes_in_S = []
    zeroes_in_T = []
    for i in range( N ):
        if S[ i ] == "0":
            zeroes_in_S.append( i )

        if T[ i ] == "0":
            zeroes_in_T.append( i )
    
    ans = 0
    for i in range( S[ : N ].count( "0" ) ):
        if zeroes_in_S[ i ] != zeroes_in_T[ i ]:
            ans += 1

    print( ans )