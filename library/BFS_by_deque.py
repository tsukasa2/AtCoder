# ABC184 E

H, W = map( int, input().split() )
a = [ "#" * ( W + 2 ) ]
for _ in range( H ):
    a.append( "#" + input() + "#" )
a.append( "#" * ( W + 2 ) )

S, G = ( 0, 0 ), ( 0, 0 )
portal = [ [] for _ in range( 26 ) ]
for i in range( 1, H + 1 ):
    for j in range( 1, W + 1 ):
        if a[ i ][ j ] == "S":
            S = ( i, j )
        elif a[ i ][ j ] == "G":
            G = ( i, j )
        elif a[ i ][ j ] != "." and a[ i ][ j ] != "#":
            portal[ ord( a[ i ][ j ] ) - 97 ].append( ( i, j ) )

INF = 10 ** 10
cost = [ [ INF for _ in range( W + 2 ) ] for _ in range( H + 2 ) ]
# visited = [ [ False for _ in range( W + 2 ) ] for _ in range( H + 2 ) ]
move = [ ( 1, 0 ), ( 0, 1 ), ( -1, 0 ), ( 0, -1 ) ]
visited_portal = [ False for _ in range( 26 ) ]

from collections import deque
cost[ S[ 0 ] ][ S[ 1 ] ] = 0
queue = deque( [ ( cost[ S[ 0 ] ][ S[ 1 ] ],  S ) ] )
while queue:
    c, ( v_h, v_w ) = queue.popleft()
    # visited[ v_h ][ v_w ] = True

    for m in move:
        u_h, u_w = ( v_h + m[ 0 ], v_w + m[ 1 ] )
        if a[ u_h ][ u_w ] != "#":
            if cost[ u_h ][ u_w ] < INF:
                continue
            if cost[ u_h ][ u_w ] > c + 1:
                cost[ u_h ][ u_w ] = c + 1
                queue.append( ( c + 1, ( u_h, u_w ) ) )

    asc = ord( a[ v_h ][ v_w ] ) - 97
    if asc >= 0:
        for u_h, u_w in portal[ asc ]:
            if cost[ u_h ][ u_w ] < INF:
                continue
            if cost[ u_h ][ u_w ] > c + 1:
                cost[ u_h ][ u_w ] = c + 1
                queue.append( ( c + 1, ( u_h, u_w ) ) )
        portal[ asc ] = []

if cost[ G[ 0 ] ][ G[ 1 ] ] < INF:
    print( cost[ G[ 0 ] ][ G[ 1 ] ] )
else:
    print( -1 )