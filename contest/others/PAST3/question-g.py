# n, x, y = map( int, input().split() )
# x = x + 200
# y = y + 200
# block = []
# for _ in range( n ):
#     b_x, b_y = map( int, input().split() )
#     block.append( [ b_x + 200, b_y + 200 ] )

# def adj( x, y ):
#     reach = []
#     if x+1 <= 400 and y+1 <= 400 and ( [ x+1, y+1 ] not in block ):
#         reach.append( [x+1, y+1] )
#     if y+1 <= 400 and ( [ x, y+1 ] not in block ):
#         reach.append( [x, y+1] )
#     if x-1 >= 0 and y+1 <= 400 and ( [ x-1, y+1 ] not in block ):
#         reach.append( [x-1, y+1] )
#     if x+1 <= 400 and ( [ x+1, y ] not in block ):
#         reach.append( [x+1, y] )
#     if x-1 >= 0 and ( [ x-1, y ] not in block ):
#         reach.append( [x-1, y] )
#     if y-1 >= 0 and ( [ x, y-1 ] not in block ):
#         reach.append( [x, y-1] )
#     return reach

# INF = 10 ** 10
# visited = [ False ] * ( 160801 )
# visited[ 80400 ] = True
# cost = [ INF ] * 160801
# cost[ 80400 ] = 0

# import heapq

# queue = [ ( cost[ 80400 ], 80400 ) ]
# while len( queue ) > 0:
#     cost_v, v = heapq.heappop( queue )
#     visited[ v ] = True
#     if cost_v > cost[ v ]:
#         continue
#     for x_n, y_n in adj( int( v/401 ), v % 401 ):  
#         if visited[ 401 * x_n + y_n ] == True:
#             continue
#         if cost[ 401 * x_n + y_n ] > cost_v + 1:
#             cost[ 401 * x_n + y_n ] = cost_v + 1
#             heapq.heappush( queue, ( cost[ 401 * x_n + y_n ], 401 * x_n + y_n ) )

# if cost[ 401 * x + y ] != INF:
#     print( cost[ 401 * x + y ] )
# else:
#     print( -1 )

#### WAが消せないから書き直し ####
n, x, y = map( int, input().split() )
x = x + 250
y = y + 250
block = []
for _ in range( n ):
    b_x, b_y = map( int, input().split() )
    b_x = b_x + 250
    b_y = b_y + 250
    block.append( b_x + 500 * b_y )

def adj( v ):
    v_x = v % 500
    v_y = v // 500
    reach = []
    if v_x + 1 <= 499 and v_y + 1 <= 499 and ( ( v_x + 1 ) + 500 * ( v_y + 1 ) not in block ):
        reach.append( ( v_x + 1 ) + 500 * ( v_y + 1 ) )
    if v_x + 1 <= 499 and ( ( v_x + 1 ) + 500 * v_y not in block ):
        reach.append( ( v_x + 1 ) + 500 * v_y )
    if v_y + 1 <= 499 and ( v_x + 500 * ( v_y + 1 ) not in block ):
        reach.append( v_x + 500 * ( v_y + 1 ) )
    if v_x - 1 >= 0 and v_y + 1 <= 499 and ( ( v_x - 1 ) + 500 * ( v_y + 1 ) not in block ):
        reach.append( ( v_x - 1 ) + 500 * ( v_y + 1 ) )
    if v_x - 1 >= 0 and ( ( v_x - 1 ) + 500 * v_y not in block ):
        reach.append( ( v_x - 1 ) + 500 * v_y  )
    if v_y - 1 >= 0 and ( v_x + 500 * ( v_y - 1 ) not in block ):
        reach.append( v_x + 500 * ( v_y - 1 ) )
    return reach

import heapq
INF = 10 ** 10
VISITED = 1
NOT_VISITED = 0
cost = [ INF ] * ( 499 + 500 * 499 + 1)
cost[ 250 + 500 * 250 ] = 0
visit = [ NOT_VISITED ] * ( 499 + 500 * 499 + 1)
visit[ 250 + 500 * 250 ] = VISITED
queue = [ ( cost[ 250 + 500 * 250 ], 250 + 500 * 250 ) ]
while len( queue ) > 0:
    c, v = heapq.heappop( queue )
    visit[ v ] = VISITED
    for u in adj( v ):
        if visit[ u ] == VISITED:
            continue
        if cost[ u ] > cost[ v ] + 1:
            cost[ u ] = cost[ v ] + 1
            heapq.heappush( queue, ( cost[ u ], u ) )

if cost[ x + 500 * y ] == INF:
    cost[ x + 500 * y ] = -1
print( cost[ x + 500 * y ] )
