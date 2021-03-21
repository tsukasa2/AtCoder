N, M = map( int, input().split() )
A = list( map( int, input().split() ) )
path = [ ( map( int, input().split() ) ) for _ in range( M ) ]

connect = [ [] for _ in range( N + 1 ) ]
for X, Y in path:
    connect[ X ].append( Y )

visited = [ False for _ in range( N + 1 ) ]
reachable = [ -10**10 for _ in range( N + 1 ) ] # reachable[ T ] = 街Tから行ける街のリスト
start = [] # スタート地点になる街候補

yasuijun = [ ( A[ i ], i + 1 ) for i in range( N ) ]
yasuijun.sort()
for a, town in yasuijun:
    if visited[ town ] == True:
        continue
    
    if len( connect[ town ] ) == 0:
        continue

    visited[ town ] = True
    start.append( town )
    queue = [ town ]
    while queue:
        v = queue.pop( 0 )
        for u in connect[ v ]:
            if visited[ u ] == False:
                reachable[ town ] = max( reachable[ town ], A[ u - 1 ] )
                queue.append( u )
                visited[ u ] = True

# print( yasuijun, reachable, connect, start )
ans = - 10 ** 10
for s in start:
    ad = reachable[ s ] - A[ s - 1 ]
    if ad > ans:
        ans = ad

print( ans )
            