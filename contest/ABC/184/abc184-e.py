# H, W = map( int, input().split() )
# a = []
# for _ in range( H ):
#     a_i = list( str( input() ) )
#     a.append( a_i )
 
# teleport = {}
# visited_tele = {} # add
# S, G = ( 0, 0 ), ( 1, 1 )
# for i in range( H ):
#     for j in range( W ):
#         if a[ i ][ j ] == "S":
#             S = ( i, j )
#         elif a[ i ][ j ] == "G":
#             G = ( i, j )
#         elif a[ i ][ j ] != "#" and a[ i ][ j ] != ".":
#             try:
#                 teleport[ a[ i ][ j ] ].append( ( i, j ) )
#             except KeyError:
#                 teleport[ a[ i ][ j ] ] = [ ( i, j ) ]
#                 visited_tele[ a[ i ][ j ] ] = False # add
 
# def connect( i, j ):
#     if a[ i ][ j ] == "#":
#         return []
 
#     cnct = []
#     if i > 0:
#         if a[ i - 1 ][ j ] != "#":
#             cnct.append( ( i - 1, j ) )
#     if j > 0:
#         if a[ i ][ j - 1 ] != "#":
#             cnct.append( ( i, j - 1 ) )
#     if i < H - 1:
#         if a[ i + 1 ][ j ] != "#":
#             cnct.append( ( i + 1, j ) )
#     if j < W - 1:
#         if a[ i ][ j + 1 ] != "#":
#             cnct.append( ( i, j + 1 ) )
 
#     # if a[ i ][ j ] == "S" or a[ i ][ j ] == "G" or a[ i ][ j ] == ".":
#     #     return cnct
#     # else:
#     #     for x in teleport[ a[ i ][ j ] ]:
#     #         cnct.append( x )
#     #     return cnct
#     return cnct
 
# connect_list = [ [ [] for _ in range( W ) ] for _ in range( H ) ]
# for i in range( H ):
#     for j in range( W ):
#         connect_list[ i ][ j ] = connect( i, j )
 
# import heapq
# queue = [ ( 0, S ) ]
# cost = [ [ 10 ** 8 for _ in range( W ) ] for _ in range( H ) ]
# cost[ S[ 0 ] ][ S[ 1 ] ] = 0
# visited = [ [ False for _ in range( W ) ] for _ in range( H ) ]
# while len( queue ) > 0:
#     c, ( v_i, v_j ) = heapq.heappop( queue )
#     visited[ v_i ][ v_j ] = True
#     for ( u_i, u_j ) in connect_list[ v_i ][ v_j ]:
#         if visited[ u_i ][ u_j ] == True:
#             continue
#         if cost[ u_i ][ u_j ] > cost[ v_i ][ v_j ] + 1:
#             cost[ u_i ][ u_j ] = cost[ v_i ][ v_j ] + 1
#             heapq.heappush( queue, ( cost[ u_i ][ u_j ], ( u_i, u_j ) ) )
    
#     if a[ v_i ][ v_j ] != "S" and a[ v_i ][ v_j ] != "G" and a[ v_i ][ v_j ] != "#" and a[ v_i ][ v_j ] != ".":
#         if visited_tele[ a[ v_i ][ v_j ] ] == True:
#             continue
#         visited_tele[ a[ v_i ][ v_j ] ] = True

#         for ( t_i, t_j ) in teleport[ a[ v_i ][ v_j ] ]:
#             if visited[ t_i ][ t_j ] == True:
#                 continue
#             if cost[ t_i ][ t_j ] > cost[ v_i ][ v_j ] + 1:
#                 cost[ t_i ][ t_j ] = cost[ v_i ][ v_j ] + 1
#                 heapq.heappush( queue, ( cost[ t_i ][ t_j ], ( t_i, t_j ) ) )
 
# if cost[ G[ 0 ] ][ G[ 1 ] ] < 10 ** 8:
#     print( cost[ G[ 0 ] ][ G[ 1 ] ] )
# else:
#     print( -1 )

H, W = map( int, input().split() )
a = []
for _ in range( H ):
    a_i = list( str( input() ) )
    a.append( a_i )

S, G = ( 0, 0 ), ( 0, 0 )
teleport = {}
used_port = {}
for i in range( H ):
    for j in range( W ):
        if a[ i ][ j ] == "S":
            S = ( i, j )
        if a[ i ][ j ] == "G":
            G = ( i, j )
        if a[ i ][ j ] != "#" and a[ i ][ j ] != ".":
            try:
                teleport[ a[ i ][ j ] ].append( ( i, j ) )
            except KeyError:
                teleport[ a[ i ][ j ] ] = [ ( i, j ) ]
                used_port[ a[ i ][ j ] ] = False

import heapq
dist = [ [ 10 ** 8 for _ in range( W ) ] for _ in range( H ) ]
dist[ S[ 0 ] ][ S[ 1 ] ] = 0
visited = [ [ False for _ in range( W ) ] for _ in range( H ) ]
queue = [ ( dist[ S[ 0 ] ][ S[ 1 ] ], S ) ]

while queue:
    c, ( v_i, v_j ) = heapq.heappop( queue )

    if visited[ v_i ][ v_j ] == True:
        continue
    visited[ v_i ][ v_j ] = True
