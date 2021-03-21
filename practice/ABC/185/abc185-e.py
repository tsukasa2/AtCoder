N, M = map( int, input().split() )
A = list( map( int, input().split() ) )
B = list( map( int, input().split() ) )

INF = 10 ** 8
dp = [ [ INF for _ in range( M + 1 ) ] for _ in range( N + 1 ) ]
# dp[ i ][ j ] = Aの[ : i ]とBの[ : j ]に対する答え

dp[ 0 ][ 0 ] = 0
for i in range( N + 1 ):
    for j in range( M + 1 ):
        # dp[ i ][ j ] = min(
        #     dp[ i - 1 ][ j ] + 1
        #         ( A[ i - 1 ]を削除する )
        #     dp[ i ][ j - 1 ] + 1
        #         ( B[ j - 1 ]を削除する )
        #     dp[ i - 1 ][ j - 1 ] + 1
        #         ( A[ i - 1 ] != B[ j - 1 ]なるA[ i - 1 ]とB[ j - 1 ]をともに残す )
        #     dp[ i - 1 ][ j - 1 ]
        #         ( A[ i - 1 ] == B[ j - 1 ]なるA[ i - 1 ]とB[ j - 1 ]をともに残す )
        # )

        # A[ i ]を削除
        if i > 0:
            dp[ i ][ j ] = min( dp[ i ][ j ], dp[ i - 1 ][ j ] + 1 )

        # B[ j ]を削除
        if j > 0:
            dp[ i ][ j ] = min( dp[ i ][ j ], dp[ i ][ j - 1 ] + 1 )

        # A[ i ]もB[ j ]も保持
        if i > 0 and j > 0:
            if A[ i - 1 ] == B[ j - 1 ]:
                dp[ i ][ j ] = min( dp[ i ][ j ], dp[ i - 1 ][ j - 1 ] )
            else:
                dp[ i ][ j ] = min( dp[ i ][ j ], dp[ i - 1 ][ j - 1 ] + 1 )

print( dp[ N ][ M ] )