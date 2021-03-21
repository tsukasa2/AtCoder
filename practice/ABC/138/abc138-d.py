N, Q = map( int, input().split() )
E = [ tuple( map( int, input().split() ) ) for _ in range( N - 1 ) ]
OP = [ tuple( map( int, input().split() ) ) for _ in range( Q ) ]

connect = [ [] for _ in range( N ) ]
for ( a, b ) in E:
    connect[ a - 1 ].append( b - 1 )
    connect[ b - 1 ].append( a - 1 )

from collections import deque
parent = [ -1 for _ in range( N ) ]
queue = deque( [ 0 ] )
visited = [ False for _ in range( N ) ]
while queue:
    v = queue.popleft()
    visited[ v ] = True
    for u in connect[ v ]:
        if visited[ u ] != True:
            parent[ u ] = v
            queue.append( u )

# print( parent )

ans = [ 0 for _ in range( N ) ]
for ( p, x ) in OP:
    p -= 1
    ans[ p ] += x

queue = deque( [ 0 ] )
while queue:
    v = queue.popleft()
    visited[ v ] = True
    for u in connect[ v ]:
        if parent[ u ] == v:
            ans[ u ] += ans[ v ]
            queue.append( u )
        
print( " ".join( map( str, ans ) ) )