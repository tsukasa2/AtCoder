N, W = map( int, input().split() )
S, T, P = [], [], []
for _ in range( N ):
    S_i, T_i, P_i = map( int, input().split() )
    S.append( S_i )
    T.append( T_i )
    P.append( P_i )

MAX_T = max( T )
used = [ 0 for _ in range( MAX_T + 1 ) ]
dused = [ 0 for _ in range( MAX_T + 1 ) ]

for i in range( N ):
    dused[ S[ i ] ] += P[ i ]
    dused[ T[ i ] ] += -P[ i ]

used_p = 0
for t in range( MAX_T + 1 ):
    used[ t ] = used_p + dused[ t ]
    used_p = used[ t ]
    # print( used, dused )
    if used[ t ] > W:
        print( "No" )
        break
else:
    print( "Yes" )