R, C = map( int, input().split() )
A = [ list( map( int, input().split() ) ) for _ in range( R ) ]
B = [ list( map( int, input().split() ) ) for _ in range( R - 1 ) ]

from heapq import heappop, heappush

INF = 10 ** 18
visit = [ [ False for _ in range( C ) ] for _ in range( R ) ]
cost = [ [ INF for _ in range( C ) ] for _ in range( R ) ]
cost[ 0 ][ 0 ] = 0
heap = [ ( cost[ 0 ][ 0 ], ( 0, 0 ) ) ]
while visit[ R - 1 ][ C - 1 ] == False:
    c, v = heappop( heap )
    x, y = v
    visit[ x ][ y ] = True
    
    if y < C - 1:
        if visit[ x ][ y + 1 ] == False:
            if cost[ x ][ y + 1 ] > c + A[ x ][ y ]:
                cost[ x ][ y + 1 ] = c + A[ x ][ y ]
                heappush( heap, ( cost[ x ][ y + 1 ], ( x, y + 1 ) ) )

    if y > 0:
        if visit[ x ][ y - 1 ] == False:
            if cost[ x ][ y - 1 ] > c + A[ x ][ y - 1 ]:
                cost[ x ][ y - 1 ] = c + A[ x ][ y - 1 ]
                heappush( heap, ( cost[ x ][ y - 1 ], ( x, y - 1 ) ) )
    
    if x < R - 1:
        if visit[ x + 1 ][ y ] == False:
            if cost[ x + 1 ][ y ] > c + B[ x ][ y ]:
                cost[ x + 1 ][ y ] = c + B[ x ][ y ]
                heappush( heap, ( cost[ x + 1 ][ y ], ( x + 1, y ) ) )
    
    for i in range( 1, x + 1 ):
        # print( x - i, y )
        if visit[ x - i ][ y ] == False:
            if cost[ x - i ][ y ] > c + ( 1 + i ):
                cost[ x - i ][ y ] = c + ( 1 + i )
                heappush( heap, ( cost[ x - i ][ y ], ( x - i, y ) ) )
    
    # print( c, v, heap )

print( cost[ R - 1 ][ C - 1 ] )
