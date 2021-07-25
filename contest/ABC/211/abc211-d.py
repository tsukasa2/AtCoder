N, M = map( int, input().split() )
AB = [ tuple( map( int, input().split() ) ) for _ in range( M ) ]
MOD = 10 ** 9 + 7

connect = [ [] for _ in range( N ) ]
for ( a, b ) in AB:
    connect[ a - 1 ].append( b - 1 )
    connect[ b - 1 ].append( a - 1 )

from collections import deque
INF = 10 ** 10
depth = [ INF ] * N
depth[ 0 ] = 0
reversed_depth = [ [] for _ in range( N ) ]
reversed_depth[ 0 ].append( 0 )
queue = deque( [ 0 ] )
while queue:
    p = queue.popleft()
    for c in connect[ p ]:
        if depth[ c ] < INF:
            continue
        else:
            depth[ c ] = depth[ p ] + 1
            reversed_depth[ depth[ c ] ].append( c )
            queue.append( c )

# print( reversed_depth )
# print( connect )

ans = [ 0 ] * N
ans[ 0 ] = 1
for i in range( 1, N ):
    for v in reversed_depth[ i ]:
        for p in connect[ v ]:
            # print( v, p, depth[ v ], depth[ p ] )
            if depth[ p ] == depth[ v ] - 1:
                ans[ v ] += ans[ p ]
                ans[ v ] %= MOD

print( ans[ N - 1 ] )