n = int( input() )
p = list( map( int, input().split() ) )

for i in range( len( p ) ):
    p[ i ] -= 1

p = [ 0 ] + p
c = [ [] for _ in range( n ) ]
for i in range( 1, n ):
    c[ p[ i ] ].append( i )

from heapq import heappush, heappop
from collections import deque
queue = deque( [ 0 ] )

leaf = [ 0 for _ in range( n ) ]
node = [ 1 for _ in range( n ) ]
depth = [ 10 ** 8 for _ in range( n ) ]
depth[ 0 ] = 0
heap = []
visited = [ False for _ in range( n ) ]

while queue:
    v = queue.popleft()
    if len( c[ v ] ) > 0:
        for nv in c[ v ]:
            queue.append( nv )
            depth[ nv ] = depth[ v ] + 1
    else:
        heappush( heap, ( -depth[ v ], v ) )
        visited[ v ] = True
        leaf[ v ] = 1

while heap:
    d, v = heappop( heap )
    if v == 0:
        break
    leaf[ p[ v ] ] += leaf[ v ]
    node[ p[ v ] ] += node[ v ]
    
    if visited[ p[ v ] ] == False:
        heappush( heap, ( -depth[ p[ v ] ], p[ v ] ) )
        visited[ p[ v ] ] = True

# print( leaf )
# print( node )

branch = [ [] for _ in range( n ) ]
for i in range( 1, n ):
    heappush( branch[ p[ i ] ], ( node[ i ], leaf[ i ], i ) )

# print( branch )

takahashi_score, aoki_score = 0, 0
locate = 0
coin = [ True for _ in range( n ) ]
while True:
    if coin[ locate ]:
        coin[ locate ] = False
        takahashi_score += 1
    else:
        if branch[ locate ]:
            lf, nd, nv = heappop( branch[ locate ] )
            locate = nv
        else:
            if locate == 0:
                break
            else:
                locate = p[ locate ]
        # print( locate + 1 )
    
    if coin[ locate ]:
        coin[ locate ] = False
        aoki_score += 1
    else:
        if branch[ locate ]:
            lf, nd, nv = heappop( branch[ locate ] )
            locate = nv
        else:
            if locate == 0:
                break
            else:
                locate = p[ locate ]
        # print( locate + 1 )
    # print( "SCORE:", takahashi_score, aoki_score )
    
    # print( locate )
    
print( takahashi_score )