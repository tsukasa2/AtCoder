h, w = map( int, input().split() )
c_h, c_w = map( int, input().split() )
c = ( c_h - 1 ) * w + ( c_w - 1 )
d_h, d_w = map( int, input().split() )
d = ( d_h - 1 ) * w + ( d_w - 1 )
s = []
for _ in range( h ):
    s_h = str( input() )
    # s.append( s_h )
    for s_h_w in s_h:
        s.append( s_h_w )

move_a = []
for i in range( h * w ):
    move_a_i = []
    if i % w > 0:
        if s[ i - 1 ] != "#":
            move_a_i.append( i - 1 )
    if i // w > 0:
        if s[ i - w ] != "#":
            move_a_i.append( i - w )
    if i % w < w - 1:
        if s[ i + 1 ] != "#":
            move_a_i.append( i + 1 )
    if i // w < h - 1:
        if s[ i + w ] != "#":
            move_a_i.append( i + w )
    move_a.append( move_a_i )

move_b = []
for i in range( h * w ):
    move_b_i = []
    if i % w > 1:
        if s[ i - 2 ] != "#":
            move_b_i.append( i - 2 )
    if i % w > 0 and i // w > 0:
        if s[ i - 1 - w ] != "#":
            move_b_i.append( i - 1 - w )
    if i % w > 1 and i // w > 1:
        if s[ i - 2 - 2 * w ] != "#":
            move_b_i.append( i - 2 - 2 * w )
    if i // w > 1:
        if s[ i - 2 * w ] != "#":
            move_b_i.append( i - 2 * w )
    if i // w > 0 and i % w < w - 1:
        if s[ i - w + 1 ] != "#":
            move_b_i.append( i - w + 1 )
    if i // w > 1 and i % w < w - 2:
        if s[ i - 2 * w + 2 ] != "#":
            move_b_i.append( i - 2 * w + 2 )
    if i % w < w - 2:
        if s[ i + 2  ] != "#":
            move_b_i.append( i + 2 )
    if i % w < w - 1 and i // w < h - 1:
        if s[ i + 1 + w ] != "#":
            move_b_i.append( i + 1 + w )
    if i % w < w - 2 and i // w < h - 2:
        if s[ i + 2 + 2 * w  ] != "#":
            move_b_i.append( i + 2 + 2 * w )
    if i // w < h - 2:
        if s[ i + 2 * w  ] != "#":
            move_b_i.append( i + 2 * w )
    if i % w > 0 and i // w < h - 1:
        if s[ i + w - 1 ] != "#":
            move_b_i.append( i + w - 1 )
    if i % w > 1 and i // w < h - 2:
        if s[ i + 2 * w - 2  ] != "#":
            move_b_i.append( i + 2 * w - 2 )

    if i % w > 2 and i // w > 0:
        if s[ i - w - 2  ] != "#":
            move_b_i.append( i - w - 2 )
    if i % w > 1 and i // w > 1:
        if s[ i - 2 * w - 1  ] != "#":
            move_b_i.append( i - 2 * w - 1 )
    if i % w < w - 1 and i // w > 2:
        if s[ i - 2 * w + 1  ] != "#":
            move_b_i.append( i - 2 * w + 1 )
    if i % w < w - 2 and i // w > 1:
        if s[ i - w + 2 ] != "#":
            move_b_i.append( i - w + 2 )
    if i % w < w - 2 and i // w < h - 1:
        if s[ i + w + 2 ] != "#":
            move_b_i.append( i + w + 2 )
    if i % w < w - 1 and i // w < h - 2:
        if s[ i + 2 * w + 1 ] != "#":
            move_b_i.append( i + 2 * w + 1 )
    if i % w > 0 and i // w < h - 2:
        if s[ i + 2 * w - 1 ] != "#":
            move_b_i.append( i + 2 * w - 1 )
    if i % w > 1 and i // w < h - 1:
        if s[ i + w - 2 ] != "#":
            move_b_i.append( i + w - 2 )
    move_b.append( move_b_i )

from heapq import heappush, heappop
INF = 10 ** 10
VISITED = 1
NOT_VISITED = 0
      
cost = [ INF ] * ( h * w )
cost[ c ] = 0
visit = [ NOT_VISITED ] * ( h * w )
visit[ c ] = VISITED
queue = [ ( cost[ c ], c ) ]
while len( queue ) > 0:
    c_v, v = heappop( queue )
    visit[ v ] = VISITED
    for u in move_a[ v ]:
        if visit[ u ] == VISITED:
            continue
        if cost[ u ] > cost[ v ]:
            cost[ u ] = cost[ v ]
            heappush( queue, ( cost[ u ], u ) )
    for t in move_b[ v ]:
        if visit[ t ] == VISITED:
            continue
        if cost[ t ] > cost[ v ] + 1:
            cost[ t ] = cost[ v ] + 1
            heappush( queue, ( cost[ t ], t ) )

if cost[ d ] == INF:
    print( -1 )
else:
    print( cost[ d ] )