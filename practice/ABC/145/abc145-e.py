N, T = map( int, input().split() )
A, B = [], []
menu = []
for _ in range( N ):
    A_i, B_i = map( int, input().split() )
    A.append( A_i )
    B.append( B_i )
    menu.append( ( A_i, B_i ) )

# menu = []
# for i in range( N ):
#     menu.append( ( A[ i ], B[ i ] ) )

menu.sort()

dp = [ [ 0 for _ in range( T + 1 ) ] for _ in range( N + 1 ) ]
for i in range( N ):
    A_i, B_i = menu[ i ]
    for j in range( T ):
        if j + A_i <= T:
            # if dp[ i + 1 ][ j + A_i ] < dp[ i ][ j ] + B_i:
            #     dp[ i + 1 ][ j + A_i ] = dp[ i ][ j ] + B_i
            dp[ i + 1 ][ j + A_i ] = max( dp[ i + 1 ][ j + A_i ], dp[ i ][ j ] + B_i )
        dp[ i + 1 ][ j ] = max( dp[ i ][ j ], dp[ i + 1 ][ j ] )

ans = 0
for i in range( N ):
    A_i, B_i = menu[ i ]
    ans = max( ans, dp[ i ][ T - 1 ] + B_i )

print( ans )