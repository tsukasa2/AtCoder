N = int( input() )
A = []
x = []
y = []
for _ in range( N ):
    A_i = int( input() )
    A.append( A_i )
    x_i = []
    y_i = []
    for _ in range( A_i ):
        x_ij, y_ij = map( int, input().split() )
        x_i.append( x_ij - 1 )
        y_i.append( y_ij )
    x.append( x_i )
    y.append( y_i )

from collections import deque
from itertools import chain, combinations
def powerset( iterable ):
    # powerset( [ 1, 2, 3 ] )
    # --> () ( 1, ) ( 2, ) ( 3, ) ( 1, 2 ) ( 1, 3 ) ( 2, 3 ) ( 1, 2, 3 )
    s = list( iterable )
    return chain.from_iterable( combinations( s, r ) for r in range( len( s ) + 1 ) )

from collections import deque
ans = -1
for p in powerset( range( N ) ):
    honest = [ 0 ] * N
    for i in p:
        honest[ i ] = 1
    
    flag = True
    for i in p:
        for x_ij, y_ij in zip( x[ i ], y[ i ] ):
            # print( honest[ x_ij ], x_ij, y_ij )
            if not honest[ x_ij ] == y_ij:
                    flag = False
    
    # print( p, honest )
    if flag:
        ans = max( ans, len( p ) )

print( ans )