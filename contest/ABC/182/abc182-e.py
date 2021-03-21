H, W, N, M = map( int, input().split() )
A, B = [], []
for _ in range( N ):
    A_i, B_i = map( int, input().split() )
    A.append( A_i )
    B.append( B_i )
C, D = [], []
for _ in range( M ):
    C_i, D_i = map( int, input().split() )
    C.append( C_i )
    D.append( D_i )

field = {}
for i in range( N ):
    field[ ( A[ i ], B[ i ] ) ] = 2
for i in range( M ):
    field[ ( C[ i ], D[ i ] ) ] = -1

ans = N
for k in range( N ):
    #W
    i, j = A[ k ], B[ k ]
    for d in range( H + 1 ):
        if i - d < 1:
            break
        else:
            try:
                if field[ ( i - d, j ) ] == -1:
                    break
            except KeyError:
                field[ ( i - d, j ) ] = 1
                ans += 1
    #D
    i, j = A[ k ], B[ k ]
    for d in range( W + 1 ):
        if j + d > W:
            break
        else:
            try:
                if field[ ( i, j + d ) ] == -1:
                    break
            except KeyError:
                field[ ( i, j + d ) ] = 1
                ans += 1
    #S
    i, j = A[ k ], B[ k ]
    for d in range( H + 1 ):
        if i + d > H:
            break
        else:
            try:
                if field[ ( i + d, j ) ] == -1:
                    break
            except KeyError:
                field[ ( i + d, j ) ] = 1
                ans += 1
    #A
    i, j = A[ k ], B[ k ]
    for d in range( W + 1 ):
        if j - d < 1:
            break
        else:
            try:
                if field[ ( i, j - d ) ] == -1:
                    break
            except KeyError:
                field[ ( i, j - d ) ] = 1
                ans += 1

# print( field )

print( ans )