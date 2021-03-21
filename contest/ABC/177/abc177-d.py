n, m = map( int, input().split() )
a = []
b = []
friend = [ [] for _ in range( n ) ]
for _ in range( m ):
    a_i, b_i = map( int, input().split() )
    a.append( a_i - 1 )
    b.append( b_i - 1 )
    friend[ a_i - 1 ].append( b_i - 1 )
    friend[ b_i - 1 ].append( a_i - 1 )

group = [ -1 for _ in range( n ) ]
group_id = 0
queue = [ i for i in range( n ) ]
visited = [ 0 for _ in range( n ) ]

while len( queue ) > 0:
    i = queue.pop( 0 )
    if visited[ i ] == 1:
        continue
    visited[ i ] = 1
    if group[ i ] == -1:
        group[ i ] = group_id
        group_id += 1
    for j in friend[ i ]:
        group[ j ] = group[ i ]
        queue.insert( 0, j )

num_v = [ 0 for _ in range( n ) ]
for i in range( n ):
    num_v[ group[ i ] ] += 1

# print( group )
# print( num_v )
print( max( num_v ) )
