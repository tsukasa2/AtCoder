n, k = map( int, input().split() )
l = []
r = []
for _ in range( k ):
    l_i, r_i = map( int, input().split() )
    l.append( l_i )
    r.append( r_i )

s = []
for i in range( k ):
    for j in range( l[ i ], r[ i ] + 1 ):
        s.append( j )

mod = 998244353

route = [ 0 for _ in range( n + 1 ) ]
# route[ k ] = マスkにたどり着く方法の数

