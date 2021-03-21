N = int( input() )
path = [ tuple( map( int, input().split() ) ) for _ in range( N - 1 ) ]
Q = int( input() )
querry = [ tuple( map( int, input().split() ) ) for _ in range( Q ) ]

connect = [ [] for _ in range( N ) ]
for p in path:
    a, b = p
    connect[ a - 1 ].append( b - 1 )
    connect[ b - 1 ].append( a - 1 )

from collections import deque

depth = [ 0 for _ in range( N ) ]
visited = [ False for _ in range( N ) ]
s = [ 0 for _ in range( N ) ]
queue = deque( [ ( 0, 0 ) ] )
while queue:
    v, d = queue.popleft()
    visited[ v ] = True
    for u in connect[ v ]:
        if visited[ u ] == False:
            depth[ u ] = d + 1
            queue.append( ( u, depth[ u ] ) )

for q in querry:
    t, e, x = q
    e -= 1
    a, b = path[ e ]
    a -= 1
    b -= 1

    if t == 2:
        a, b = b, a
     
    if depth[ a ] > depth[ b ]:
        s[ a ] += x
    else:
        s[ 0 ] += x
        s[ b ] -= x

ans = [ s[ i ] for i in range( N ) ]
visited = [ False for _ in range( N ) ]
queue = deque( [ ( 0, s[ 0 ] ) ] )
while queue:
    v, c = queue.popleft()
    visited[ v ] = True
    for u in connect[ v ]:
        if visited[ u ] == False:
            ans[ u ] += c
            queue.append( ( u, ans[ u ] ) )

# print( connect )
# print( depth )
# print( s )
print( "\n".join( map( str, ans ) ) )