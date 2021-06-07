N = int( input() )
T = list( map( int, input().split() ) )

sum_T = sum( T )
L, R = 0, 100 * 10 ** 3 + 100
while R - L > 1:
    M = ( L + R ) // 2
    # dp = [ [ 0 for _ in range( M + 1 ) ] for _ in range( N + 1 ) ]
    dp = [ [ 0 ] * ( M + 1 ) for _ in range( N + 1 ) ]
    for i in range( N ):
        for j in range( 1, M + 1 ):
            if T[ i ] <= j:
                dp[ i + 1 ][ j ] = max( dp[ i ][ j ], dp[ i ][ j - T[ i ] ] + T[ i ] )
    
    # print( dp )
    # print( M, dp[ N ][ M ], sum_T )
    if sum_T - dp[ N ][ M ] <= M:
        R = M
    else:
        L = M

print( R )