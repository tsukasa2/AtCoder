import sys
sys.setrecursionlimit( 10 ** 9 )
from collections import deque

N, M = map( int, input().split() )
AB = [ tuple( map( int, input().split() ) ) for _ in range( M ) ]

connect = [ [] for _ in range( N ) ]
for ( a, b ) in AB:
    connect[ a - 1 ].append( b - 1 )
    connect[ b - 1 ].append( a - 1 )

dim = [ 0 for _ in range( N ) ]
visited = [ False for _ in range( N ) ]
added = [ False for _ in range( N ) ]
added[ 0 ] = True
queue = deque( [ 0 ] )
hoketsu = 0
ans = 1
while queue:
    v = queue.popleft()
    visited[ v ] = True
    ans *= max( 0, 3 - dim[ v ] )

    for u in connect[ v ]:
        if visited[ u ] == False:
            dim[ u ] += 1
        
        if added[ u ] == False:
            queue.append( u )
            added[ u ] = True
    
    if len( queue ) == 0:
        while hoketsu < N:
            if added[ hoketsu ] == False:
                queue.append( hoketsu )
                added[ hoketsu ] = True
                break
            hoketsu += 1

# print( connect, visited, dim )
print( ans )