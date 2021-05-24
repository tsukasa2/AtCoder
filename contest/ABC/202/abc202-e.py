N = int( input() )
P = list( map( int, input().split() ) )
Q = int( input() )
Query = [ tuple( map( int, input().split() ) ) for _ in range( Q ) ]

child = { i : [] for i in range( N ) }
for i in range( 1, N ):
    child[ P[ i - 1 ] - 1 ].append( i )

depth = [ -1 for _ in range( N ) ]
depth[ 0 ] = 0

from collections import deque
queue = deque( [ ( depth[ 0 ], 0 ) ] )
while queue:
    d, p = queue.popleft()

    for c in child[ p ]:
        depth[ c ] = d + 1
        queue.append( ( depth[ c ], int( c ) ) )

print( depth )

from collections import Counter
from_here = [ Counter() for _ in range( N ) ]
# from_here[ v ][ d ] = vからd歩先にある頂点の数

queue = [ ( - depth[ i ], i ) for i in range( N ) ]
queue.sort()
for ( d, v ) in queue:
    d *= -1
    