import sys

sys.setrecursionlimit( 10 ** 8 )

N, M = map( int, input().split() )
u, v, c = [], [], []
for _ in range( M ):
    u_i, v_i, c_i = map( int, input().split() )
    u.append( u_i )
    v.append( v_i )
    c.append( c_i )

connect = [ [] for _ in range( N ) ]
for i in range( M ):
    connect[ u[ i ] - 1 ].append( v[ i ] - 1 )
    connect[ v[ i ] - 1 ].append( u[ i ] - 1 )

label = [ {} for _ in range( N ) ]
for i in range( M ):
    label[ u[ i ] - 1 ][ v[ i ] - 1 ] = c[ i ] - 1
    label[ v[ i ] - 1 ][ u[ i ] - 1 ] = c[ i ] - 1

write = [ 0 for _ in range( N ) ]
visited = [ False for _ in range( N ) ]
def search( p ):
    for q in connect[ p ]:
        if visited[ q ] == True:
            continue
        else:
            visited[ q ] = True

            if label[ p ][ q ] == write[ p ]:
                write[ q ] = ( write[ p ] + 1 ) % N
            else:
                write[ q ] = label[ p ][ q ]
            
            search( q )

visited[ 0 ] = True
search( 0 )

for i in range( N ):
    print( write[ i ] + 1 )