# N = int( input() )
# A = []
# for _ in range( N ):
#     A_i = list( map( int, input().split() ) )
#     A_i.append( -1 )
#     A.append( A_i )

# opponent = [ [ A[ i ][ 0 ], 0 ] for i in range( N ) ]
# days = 0

# import copy
# while True:
#     progress = False
#     complete = True
#     today_opponent = copy.deepcopy( opponent )
#     for i in range( N ):
#         op, j = today_opponent[ i ]
#         op -= 1
#         if j < N - 1:
#             complete = False
#             op_op, _ = today_opponent[ op ]
#             op_op -= 1
#             if op_op == i:
#                 opponent[ i ][ 0 ] = A[ i ][ j + 1 ]
#                 opponent[ i ][ 1 ] = j + 1
#                 progress = True
#         # print( "TEST: ", progress, complete, i, op, j )

#     if complete == True:
#         print( days )
#         break
#     else:
#         days += 1

#     if progress == False:
#         print( -1 )
#         break

N = int( input() )
game_id = [ [ -1 for _ in range( N ) ] for _ in range( N ) ]
next_id = 0
for i in range( N ):
    for j in range( i + 1, N ):
        game_id[ i ][ j ] = next_id
        game_id[ j ][ i ] = next_id
        next_id += 1

A = [ [ int( x ) - 1 for x in input().split() ] for _ in range( N ) ]

# トポロジカルソート
from collections import defaultdict, deque

outs = defaultdict( list )
ins = defaultdict( int )
for i in range( N ):
    for j in range( N - 2 ):
        today_op = A[ i ][ j ]
        tomorrow_op = A[ i ][ j + 1 ]
        today_game = game_id[ i ][ today_op ]
        tomorrow_game = game_id[ i ][ tomorrow_op ]
        outs[ today_game ].append( tomorrow_game )
        ins[ tomorrow_game ] += 1

q = deque( v for v in range( N * ( N - 1 ) // 2 ) if ins[ v ] == 0 )
res = []
depth = [ 0 for _ in range( N * ( N - 1 ) // 2 ) ]
while q:
    v1 = q.popleft()
    res.append( depth[ v1 ] )
    for v2 in outs[ v1 ]:
        ins[ v2 ] -= 1
        depth[ v2 ] = max( depth[ v2 ], depth[ v1 ] + 1 )
        if ins[ v2 ] == 0:
            q.append( v2 )

if len( res ) == N * ( N - 1 ) // 2:
    print( max( res ) + 1 )
else:
    print( -1 )
