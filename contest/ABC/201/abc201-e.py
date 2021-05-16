N = int( input() )
uvw = [ tuple( map( int, input().split() ) ) for _ in range( N - 1 ) ]

INF = 10 ** 18
dist = [ [ 0 for _ in range( N ) ] for _ in range( N ) ]
connect = [ [] for _ in range( N ) ]
cost = [ [ INF for _ in range( N ) ] for _ in range( N ) ]
for ( u, v, w ) in uvw:
    cost[ u - 1 ][ v - 1 ] = w
    connect[ u - 1 ].append( v - 1 )
    cost[ v - 1 ][ u - 1 ] = w
    connect[ v - 1 ].append( u - 1 )

from collections import deque
for root in range( N ):
    visited = [ False for _ in range( N ) ]
    visited[ root ] = True
    queue = deque( [ root ] )
    while queue:
        v = queue.popleft()

        for u in connect[ v ]:
            if visited[ u ] == False:
                visited[ u ] = True
                dist[ root ][ u ] = dist[ root ][ v ] ^ cost[ v ][ u ]
                queue.append( u )

ans = 0
MOD = 10 ** 9 + 7
for i in range( N ):
    for j in range( N ):
        ans += dist[ i ][ j ]
        ans %= MOD

print( ans * pow( 2, -1, MOD ) % MOD )