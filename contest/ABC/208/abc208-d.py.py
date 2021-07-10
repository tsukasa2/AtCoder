N, M = map( int, input().split() )
ABC = [ tuple( map( int, input().split() ) ) for _ in range( M ) ]

INF = 10 ** 10
f_0 = [ [ INF ] * ( N + 1 ) for _ in range( N + 1 ) ]

for i in range( N + 1 ):
    f_0[ i ][ i ] = 0

for a, b, c in ABC:
    f_0[ a ][ b ] = c

ans = 0
for k in range( 1, N + 1 ):
    f = [ [ INF ] * ( N + 1 ) for _ in range( N + 1 ) ]
    for s in range( 1, N + 1 ):
        for t in range( 1, N + 1 ):
            f[ s ][ t ] = min(
                f_0[ s ][ k ] + f_0[ k ][ t ],
                f_0[ s ][ t ]
            )
            if f[ s ][ t ] < INF:
                ans += f[ s ][ t ]

    f_0 = f

print( ans )