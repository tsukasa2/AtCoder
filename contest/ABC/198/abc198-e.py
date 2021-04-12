from collections import deque
import copy

N = int( input() )
C = list( map( int, input().split() ) )
AB = [ tuple( map( int, input().split() ) ) for _ in range( N - 1 ) ]

connect = [ [] for _ in range( N ) ]
for ( a, b ) in AB:
    connect[ a - 1 ].append( b - 1 )
    connect[ b - 1 ].append( a - 1 )

INF = 10 ** 10
cost = [ INF for _ in range( N ) ]
cost[ 0 ] = 0

found_color = [ set() for _ in range( N ) ]

queue = deque( [ ( cost[ 0 ], 0 ) ] )

ans = []

while queue:
    c, v = queue.popleft()

    if C[ v ] not in found_color[ v ]:
        ans.append( v )
    
    for u in connect[ v ]:
        if cost[ u ] < INF:
            continue
        else:
            cost[ u ] = c + 1
            found_color[ u ] = copy.copy( found_color[ v ] )
            found_color[ u ].add( C[ v ] )
            queue.append( ( cost[ u ], u ) )

# print( found_color )
ans.sort()
for v in ans:
    print( v + 1 )