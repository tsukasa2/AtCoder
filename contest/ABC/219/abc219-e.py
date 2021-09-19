from itertools import chain, combinations
def powerset( iterable ):
    # powerset( [ 1, 2, 3 ] )
    # --> () ( 1, ) ( 2, ) ( 3, ) ( 1, 2 ) ( 1, 3 ) ( 2, 3 ) ( 1, 2, 3 )
    s = list( iterable )
    return chain.from_iterable( combinations( s, r ) for r in range( len( s ) + 1 ) )

from collections import deque

def judge( dots ):
    N = len( dots )
    dots_list = list( dots )
    reverse_dots = { d : i for i, d in enumerate( dots_list ) }
    visited = [ False ] * N

    move = [ ( -1, 0 ), ( 0, -1 ), ( 0, 1 ), ( 1, 0 ) ]
    visited[ 0 ] = True
    queue = deque( [ 0 ] )
    while queue:
        v = queue.popleft()
        x, y = dots_list[ v ]
        for ( dx, dy ) in move:
            if ( x + dx, y + dy ) in reverse_dots.keys():
                u = reverse_dots[ ( x + dx, y + dy ) ]
                if visited[ u ] == False:
                    visited[ u ] = True
                    queue.append( u )

    if False in visited:
        return False
    else:
        return True


A = [ tuple( map( int, input().split() ) ) for _ in range( 4 ) ]

all_dots = set( ( i, j ) for i in range( -1, 5 ) for j in range( -1, 5 ) )
dots = powerset( [ ( i, j ) for i in range( 4 ) for j in range( 4 ) ] )

ans = 0
for i, d in enumerate( dots ):
    # print( i )
    flag = False
    for i in range( 4 ):
        for j in range( 4 ):
            if A[ i ][ j ] == 1:
                if not ( i, j ) in d:
                    flag = True
    
    if flag:
        continue
    
    # print( set( d ) )
    # print( set( all_dots ) )
    # print( set( all_dots ) - set( d ) )
    if judge( d ) and judge( set( all_dots ) - set( d  )):
        ans += 1

print( ans )