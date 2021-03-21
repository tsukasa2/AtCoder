# import copy
# n, m = map( int, input().split() )
# connect = []

# for _ in range( n+1 ):
#     connect.append( [ 0 ] * ( n+1 ) )

# for _ in range( m ):
#     a, b = map( int, input().split() )
#     connect[ a ][ b ] = 1
#     connect[ b ][ a ] = 1

# guide = [ 0 ] * ( n+1 )
# path = [ 0, 0 ] + [ m+1 ] * ( n-1 )
# unvisited = [ a for a in range( 1, n+1 ) ]

# def solve( a, unvisited ): # aに隣接したやつのguideをaにする．またそれのpathをpath[a]+1にする．
#     for b in unvisited:
#         if connect[a][b] == 1 and path[a] + 1 < path[b]:
#             path[b] = path[a] + 1
#             guide[b] = a
#     next_unvisited = copy.deepcopy( unvisited )
#     next_unvisited.remove( a )
#     for b in unvisited:
#         if connect[a][b] == 1:
#             solve( b, next_unvisited )

# solve( 1, unvisited )

# if 0 not in guide[2:]:
#     print( "Yes" )
#     for i in range( 2, n+1 ):
#         print( guide[i] )
# else:
#     print( "No" )

####以下カンニング####
n, m = map( int, input().split() )
connect = {}

for _ in range( m ):
    a, b = map( int, input().split() )
    try:
        connect[ a ].append( b )
    except KeyError:
        connect[ a ] = [ b ]
    try:
        connect[ b ].append( a )
    except KeyError:
        connect[ b ] = [ a ]

queue = [ 1 ]
guide = [ -1 ] * ( n+1 )
visited = [ False ] * ( n+1 )

while queue:
    x = queue.pop(0)
    for y in connect[ x ]:
        if visited[ y ] == False:
            queue.append( y )
            guide[ y ] = x
            visited[ y ] = True

print( "Yes" )
for x in range( 2, n+1 ):
    print( guide[x] )