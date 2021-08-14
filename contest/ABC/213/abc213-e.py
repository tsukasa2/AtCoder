H, W = map( int, input().split() )
S = [ str( input() ) for _ in range( H ) ]

import heapq
INF = 10 ** 10
visited = [ [ False ] * W for _ in range( H ) ]
cost = [ [ INF ] * W for _ in range( H ) ]
cost[ 0 ][ 0 ] = 0
queue = [ ( cost[ 0 ][ 0 ], ( 0, 0 ) ) ]
adj = [ ( -1, 0 ), ( 0, -1 ), ( 0, 1 ), ( 1, 0 ) ]
while queue:
    c, v = heapq.heappop( queue )
    h, w = v
    visited[ h ][ w ] = True

    for ( i, j ) in adj:
        if h + i >= 0 and h + i < H:
            if w + j >= 0 and w + j < W:
                if visited[ h + i ][ w + j ]:
                    continue
                else:
                    if cost[ h + i ][ w + j ] > c and S[ h + i ][ w + j ] == ".":
                        cost[ h + i ][ w + j ] = c
                        heapq.heappush( queue, ( c, ( h + i, w + j ) ) )
    
    for i in [ -2, -1, 0, 1, 2 ]:
        for j in [ -2, -1, 0, 1, 2 ]:
            if abs( i ) + abs( j ) == 4:
                continue

            if h + i >= 0 and h + i < H:
                if w + j >= 0 and w + j < W:
                    if visited[ h + i ][ w + j ]:
                        continue
                    else:
                        if cost[ h + i ][ w + j ] > c + 1 and S[ h + i ][ w + j ] == "#":
                            cost[ h + i ][ w + j ] = c + 1
                            heapq.heappush( queue, ( c + 1, ( h + i, w + j ) ) )

# print( *cost, sep="\n" )
print( cost[ H - 1 ][ W - 1 ] )