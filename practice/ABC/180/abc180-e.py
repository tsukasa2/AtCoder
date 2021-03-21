N = int( input() )
X, Y, Z = [], [], []
for _ in range( N ):
    X_i, Y_i, Z_i = map( int, input().split() )
    X.append( X_i )
    Y.append( Y_i )
    Z.append( Z_i )

def dist( i, j ):
    a, b, c = X[ i ], Y[ i ], Z[ i ]
    p, q, r = X[ j ], Y[ j ], Z[ j ]
    return abs( p - a ) + abs( q - b ) + max( 0, r - c )

INF = 10 ** 12
bitDP = [ [ INF for _ in range( N ) ] for _ in range( 1 << N ) ]
# bitDP[ A ][ u ] = 集合Aに含まれる都市を通ってvに行くための最小コスト
# A = N桁のbit列
bitDP[ 1 ][ 0 ] = 0
for A in range( 1, 1 << N ):
    for u in range( N ):
        for v in range( N ):
            # 集合Aに含まれる都市を訪問済みで，現在地はu
            # この状態で，vに行くための最小コストを更新できるか検討
            if u == v:
                continue

            new_A = A | ( 1 << v )
            
            if bitDP[ new_A ][ v ] > bitDP[ A ][ u ] + dist( u, v ):
                bitDP[ new_A ][ v ] = bitDP[ A ][ u ] + dist( u, v )

ans = INF
for i in range( 1, N ):
    if ans > bitDP[ 2 ** N - 1 ][ i ] + dist( i, 0 ):
        ans = bitDP[ 2 ** N - 1 ][ i ] + dist( i, 0 )

print( ans )