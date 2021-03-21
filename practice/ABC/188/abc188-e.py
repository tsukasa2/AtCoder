N, M = map( int, input().split() )
A = list( map( int, input().split() ) )
path = [ ( map( int, input().split() ) ) for _ in range( M ) ]

connect = [ [] for _ in range( N ) ]
for p in path:
    X, Y = p
    connect[ X - 1 ].append( Y )

INF = 10 ** 10
dp = [ -INF for _ in range( N ) ]
# dp[ i ] = 街i+1から出発したときの売却価格の最大値

for i in reversed( range( N ) ):
    for j in connect[ i ]:
        dp[ i ] = max( dp[ i ], dp[ j - 1 ], A[ j - 1 ] )

for i in range( N ):
    dp[ i ] -= A[ i ]

print( max( dp ) )