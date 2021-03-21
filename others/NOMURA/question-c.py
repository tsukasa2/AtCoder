n = int( input() )
a = list( map( int, input().split() ) )

if n == 0 and a[0] > 1:
    print( -1 )
    exit()

sum_a = [ sum( a ) ]
for d in range( 1, n + 1 ):
    sum_a_next = sum_a[ -1 ] - a[ d - 1 ]
    sum_a.append( sum_a_next )

d_vertex = [ 0 for d in range( n + 1 ) ]

d_vertex[ 0 ] = 1
num_of_v = d_vertex[ 0 ]
for d in range( 1, n + 1 ):
    d_vertex[ d ] = min( sum_a[d], ( d_vertex[ d - 1 ] - a[ d - 1 ] ) * 2 )
    if d_vertex[ d ] <= 0:
        print( -1 )
        exit()
    num_of_v += d_vertex[ d ]

if d_vertex[ n ] < a[ n ]:
    print( -1 )
    exit()

print( num_of_v )