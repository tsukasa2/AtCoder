N, M = map( int, input().split() )
k = []
a = []
for _ in range( M ):
    k_i = int( input() )
    a_i = list( map( int, input().split() ) )
    k.append( k_i )
    a.append( a_i )

from collections import defaultdict, deque

outs = defaultdict( list )
ins = defaultdict( int )
for i in range( M ):
    for j in range( k[ i ] - 1 ):
        v1, v2 = a[ i ][ j ] - 1, a[ i ][ j + 1 ] - 1
        outs[ v1 ].append( v2 )
        ins[ v2 ] += 1

q = deque( v1 for v1 in range( N ) if ins[ v1 ] == 0 )
res = []
while q:
    v1 = q.popleft()
    res.append( v1 )
    for v2 in outs[ v1 ]:
        ins[ v2 ] -= 1
        if ins[ v2 ] == 0:
            q.append( v2 )

# print( *res, sep = ", " )
if len( res ) == N:
    print( "Yes" )
else:
    print( "No" )