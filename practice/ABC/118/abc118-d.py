N, M = map( int, input().split() )
A = list( map( int, input().split() ) )

cost = [ 10 ** 4 + 100, 2, 5, 5, 4, 5, 6, 3, 7, 6 ]

DP = [ - 10 ** 12 ] * ( N + 100 )
DP[ 0 ] = 0
# DP[ i ] = ちょうどi本のマッチを使って作ることのできる数字のうち最も大きいもの

for i in range( 1, N + 1 ):
    for A_j in A:
        if cost[ A_j ] <= i:
            DP[ i ] = max( DP[ i ], DP[ i - cost[ A_j ] ] * 10 + A_j )

print( DP[ N ] )