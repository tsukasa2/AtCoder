import sys
sys.setrecursionlimit( 10 ** 6 )

N, M = map( int, input().split() )
a = list( map( int, input().split() ) )
b = list( map( int, input().split() ) )
c, d = [], []
connect = [ [] for _ in range( N ) ]
for _ in range( M ):
    c_i, d_i = map( int, input().split() )
    c.append( c_i )
    d.append( d_i )
    connect[ c_i - 1 ].append( d_i - 1 )
    connect[ d_i - 1 ].append( c_i - 1 )

visited = [ False for _ in range( N ) ]
subgraph = [ -1 for _ in range( N ) ]
new_subgraph_id = 0

def search( v, subgraph_id ):
    visited[ v ] = True
    subgraph[ v ] = subgraph_id
    for w in connect[ v ]:
        if visited[ w ] == False:
            search( w, subgraph_id )

for v in range( N ):
    if visited[ v ] == True:
        continue
    search( v, new_subgraph_id )
    new_subgraph_id += 1

# for i in range( N ):
#     print( i + 1, -subgraph[ i ] )

sum_a = [ 0 for _ in range( N ) ]
sum_b = [ 0 for _ in range( N ) ]

for i in range( N ):
    sum_a[ subgraph[ i ] ] += a[ i ]
    sum_b[ subgraph[ i ] ] += b[ i ]

for i in range( N ):
    if sum_a[ i ] != sum_b[ i ]:
        print( "No" )
        break
else:
    print( "Yes" )