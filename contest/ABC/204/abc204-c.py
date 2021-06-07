from collections import deque

N, M = map( int, input().split() )
route = [ tuple( map( int, input().split() ) ) for _ in range( M ) ]

connect = [ [] for _ in range( N ) ]
for ( a, b ) in route:
    connect[ a - 1 ].append( b - 1 )

ans = 0
for start in range( N ):
    visited = [ 0 for _ in range( N ) ]
    visited[ start ] = 1

    queue = deque( [ start ] )
    while queue:
        v = queue.popleft()
        ans += 1

        for u in connect[ v ]:
            if visited[ u ] == 1:
                continue

            visited[ u ] = 1
            queue.append( u )

print( ans )