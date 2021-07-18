H, W, C = map( int, input().split() )
A = [ tuple( map( int, input().split() ) ) for _ in range( H ) ]

# 右下に向けてDP
INF = 10 ** 18
dp = [ [ INF ] * ( W + 1 ) for _ in range( H + 1 ) ]
for i in range( 1, H + 1 ):
    for j in range( 1, W + 1 ):
        dp[ i ][ j ] = min(
            [
                A[ i - 1 ][ j - 1 ],
                dp[ i - 1 ][ j ] + C,
                dp[ i ][ j - 1 ] + C
            ]
        )

X = [ [ INF ] * ( W + 1 ) for _ in range( H + 1 ) ]
for i in range( 1, H + 1 ):
    for j in range( 1, W + 1 ):
        X[ i ][ j ] = min(
            [
                dp[ i - 1 ][ j ] + C + A[ i - 1 ][ j - 1 ],
                dp[ i ][ j - 1 ] + C + A[ i - 1 ][ j - 1 ]
            ]
        )

ans = min( [ min( x ) for x in X ] )

# 左下に向けてDP
dp = [ [ INF ] * ( W + 1 ) for _ in range( H + 1 ) ]
for i in range( 1, H + 1 ):
    for j in reversed( range( W ) ):
        dp[ i ][ j ] = min(
            [
                A[ i - 1 ][ j ],
                dp[ i - 1 ][ j ] + C,
                dp[ i ][ j + 1 ] + C
            ]
        )

X = [ [ INF ] * ( W + 1 ) for _ in range( H + 1 ) ]
for i in range( 1, H + 1 ):
    for j in reversed( range( W ) ):
        X[ i ][ j ] = min(
            [
                dp[ i - 1 ][ j ] + C + A[ i - 1 ][ j ],
                dp[ i ][ j + 1 ] + C + A[ i - 1 ][ j ]
            ]
        )

ans = min( ans, min( [ min( x ) for x in X ] ) )

print( ans )