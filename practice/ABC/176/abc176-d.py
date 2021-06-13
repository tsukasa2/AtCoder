H, W = map( int, input().split() )
C_h, C_w = map( int, input().split() )
D_h, D_w = map( int, input().split() )
S = [ str( input() ) for _ in range( H ) ]

C_h -= 1
C_w -= 1
D_h -= 1
D_w -= 1

def connect( v ):
    res = []
    v_h, v_w = v
    for h in range( max( 0, v_h - 2 ), min( H - 1, v_h + 2 ) + 1 ):
        for w in range( max( 0, v_w - 2 ), min( W - 1, v_w + 2 ) + 1 ):
            if S[ h ][ w ] == ".":
                if abs( h - v_h ) + abs( w - v_w ) < 2:
                    res.append( ( 0, ( h, w ) ) )
                else:
                    res.append( ( 1, ( h, w ) ) )
    
    return res

import heapq
INF = 10 ** 10
visited = [ [ False ] * W for _ in range( H ) ]
cost = [ [ INF ] * W for _ in range( H ) ]
cost[ C_h ][ C_w ] = 0
queue = [ ( cost[ C_h ][ C_w ], ( C_h, C_w ) ) ]
while queue:
    c, v = heapq.heappop( queue )
    v_h, v_w = v
    visited[ v_h ][ v_w ] = True
    for c_vu, ( u_h, u_w ) in connect( v ):
        if not visited[ u_h ][ u_w ]:
            if cost[ u_h ][ u_w ] > c + c_vu:
                cost[ u_h ][ u_w ] = c + c_vu
                heapq.heappush( queue, ( c + c_vu, ( u_h, u_w ) ) )

if cost[ D_h ][ D_w ] == INF:
    print( -1 )
else:
    print( cost[ D_h ][ D_w ] )