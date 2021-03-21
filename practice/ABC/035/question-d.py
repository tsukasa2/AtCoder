# n, m, t = map( int, input().split() )
# advantage = [ 0 ] + list( map( int, input().split() ) )
# a = [ 0 ]
# b = [ 0 ]
# c = [ 0 ]
# for _ in range( m ):
#     a_i, b_i, c_i = map( int, input().split() )
#     a.append( a_i )
#     b.append( b_i )
#     c.append( c_i )

# INF = 10 ** 15
# VISITED = 1
# NOT_VISITED = 0
# connect_list = {}   # connect_list[a][b] is the cost for a -> b
# return_list = {}    # return_list[a][b] is the cost for a <- b
# for i in range( 1, m+1 ):
#     try:
#         connect_list[ a[ i ] ][ b[ i ] ] = c[ i ]
#     except KeyError:
#         connect_list[ a[ i ] ] = {}
#         connect_list[ a[ i ] ][ b[ i ] ] = c[ i ]
#     try:
#         return_list[ b[ i ] ][ a[ i ] ] = c[ i ]
#     except KeyError:
#         return_list[ b[ i ] ] = {}
#         return_list[ b[ i ] ][ a[ i ] ] = c[ i ]

# # print( connect_list )
# # print( return_list )

# cost_f = [ 0, 0 ] + [ INF ] * ( n - 1 )
# visit = [ NOT_VISITED ] * ( n + 1 )
# x = 1
# while True:
#     min_cost = INF
#     for i in range( 1, n+1 ):
#         if visit[ i ] == NOT_VISITED and cost_f[ i ] < min_cost:
#             x = i
#             min_cost = cost_f[ i ]
#     if min_cost == INF and x != 1:
#         break
#     visit[ x ] = VISITED
#     for i in connect_list[ x ].keys():
#         if cost_f[ i ] > cost_f[ x ] + connect_list[ x ][ i ]:
#             cost_f[ i ] = cost_f[ x ] + connect_list[ x ][ i ]

# cost_b = [ 0, 0 ] + [ INF ] * ( n - 1 )
# visit = [ NOT_VISITED ] * ( n + 1 )
# x = 1
# while True:
#     min_cost = INF
#     for i in range( 1, n+1 ):
#         if visit[ i ] == NOT_VISITED and cost_b[ i ] < min_cost:
#             x = i
#             min_cost = cost_b[ i ]
#     if min_cost == INF and x != 1:
#         break
#     visit[ x ] = VISITED
#     for i in return_list[ x ].keys():
#         if cost_b[ i ] > cost_b[ x ] + return_list[ x ][ i ]:
#             cost_b[ i ] = cost_b[ x ] + return_list[ x ][ i ]

# # print( cost_f[1:] )
# # print( cost_b[1:] )

# best_ad = 0
# for i in range( 1, n+1 ):
#     free = t - ( cost_f[ i ] + cost_b[ i ] )
#     if free < 0:
#         continue
#     ad = free * advantage[ i ]
#     if best_ad < ad:
#         best_ad = ad

# print( best_ad )

####以下，ヒープでやり直したもの####
from heapq import heappush, heappop
INF = 10 ** 10
VISITED = 1
NOT_VISITED = 0

n, m, t = map( int, input().split() )
advantage = [ 0 ] + list( map( int, input().split() ) )
connect_list = [[] for v in range( n+1 ) ]
return_list = [[] for v in range( n+1 ) ]
for _ in range( m ):
    a_i, b_i, c_i = map( int, input().split() )
    connect_list[ a_i ].append( ( b_i, c_i ) )
    return_list[ b_i ].append( ( a_i, c_i ) )
      
cost = [ 0, 0 ] + [ INF ] * ( n - 1 )
visit = [ NOT_VISITED ] * ( n + 1 )
queue = [ ( cost[1], 1 ) ]
while len( queue ) > 0:
    c, v = heappop( queue )
    visit[ v ] = VISITED
    for u, cost_vu in connect_list[v]:
        if visit[ u ] == VISITED:
            continue
        if cost[u] > cost[v] + cost_vu:
            cost[u] = cost[v] + cost_vu
            heappush( queue, ( cost[u], u ) )

return_cost = [ 0, 0 ] + [ INF ] * ( n - 1 )
visit = [ NOT_VISITED ] * ( n + 1 )
queue = [ ( return_cost[1], 1 ) ]
while len( queue ) > 0:
    c, v = heappop( queue )
    visit[ v ] = VISITED
    for u, cost_vu in return_list[v]:
        if visit[ u ] == VISITED:
            continue
        if return_cost[u] > return_cost[v] + cost_vu:
            return_cost[u] = return_cost[v] + cost_vu
            heappush( queue, ( return_cost[u], u ) )

best_ad = 0
for i in range( 1, n+1 ):
    free = t - ( cost[ i ] + return_cost[ i ] )
    ad = free * advantage[ i ]
    if best_ad < ad:
        best_ad = ad

print( best_ad )