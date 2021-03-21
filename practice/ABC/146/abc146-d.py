import sys
sys.setrecursionlimit( 10 ** 9 )

N = int( input() )
a, b = [], []
deg = [ 0 for _ in range( N ) ]
connect = [ [] for _ in range( N ) ]
for _ in range( N - 1 ):
    a_i, b_i = map( int, input().split() )
    a_i -= 1
    b_i -= 1
    a.append( a_i )
    b.append( b_i )
    deg[ a_i ] += 1
    deg[ b_i ] += 1
    connect[ a_i ].append( b_i )
    connect[ b_i ].append( a_i )

num_of_color = max( deg )  

# edge_color = [ [ -1 for _ in range( N ) ] for _ in range( N ) ]
edge_color = {}
visited = [ False for _ in range( N ) ]
def color_child( parent, parent_color ):
    next_color = ( parent_color + 1 ) % num_of_color
    for child in connect[ parent ]:
        if visited[ child ] == True:
            continue
        visited[ child ] = True
        # edge_color[ parent ][ child ] = next_color
        # edge_color[ child ][ parent ] = next_color
        edge_color[ ( parent, child ) ] = next_color
        edge_color[ ( child, parent ) ] = next_color
        color_child( child, next_color )
        next_color = ( next_color + 1 ) % num_of_color

visited[ a[ 0 ] ] = True
color_child( a[ 0 ], -1 )

print( num_of_color )
for i in range( N - 1 ):
    # print( edge_color[ a[ i ] ][ b[ i ] ] + 1 )
    print( edge_color[ ( a[ i ], b[ i ] ) ] + 1 )