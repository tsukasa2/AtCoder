import itertools
import heapq

M = int( input() )
uv = [ tuple( map( int, input().split() ) ) for _ in range( M ) ]
p = list( map( int, input().split() ) )

for i in range( 8 ):
    p[ i ] -= 1

for i in range( 9 ):
    if not i in p:
        p.append( i )
        break

l = [ 0, 1, 2, 3, 4, 5, 6, 7, 8 ]
vertex = []
mapping = {}
for i, per in enumerate( itertools.permutations( l, 9 ) ):
    v = "".join( map( str, per ) )
    vertex.append( v )
    mapping[ v ] = i

connect = [ [] for _ in range( 9 ) ]
for u, v in uv:
    connect[ u - 1 ].append( v - 1 )
    connect[ v - 1 ].append( u - 1 )

def arrow( v ):
    v1 = vertex[ v ]
    u = v1[ -1 ]
    res = []
    for w in connect[ int( u ) ]:
        v2 = []
        for i in range( 9 ):
            if v1[ i ] == str( w ):
                v2.append( str( u ) )
            elif v1[ i ] == str( u ):
                v2.append( str( w ) )
            else:
                v2.append( v1[ i ] )

        v2 = "".join( v2 )
        res.append( mapping[ v2 ] )
    
    return res

visited = [ 0 ] * 362880
cost = [ 10 ** 18 ] * 362880
s = "012345678"
cost[ mapping[ s ] ] = 0
queue = [ ( cost[ mapping[ s ] ], mapping[ s ] ) ]
while queue:
    c, v = heapq.heappop( queue )
    visited[ v ] = 1
    for u in arrow( v ):
        if visited[ u ] == 1:
            continue
        
        if cost[ u ] > c + 1:
            cost[ u ] = c + 1
            heapq.heappush( queue, ( cost[ u ], u ) )

ans = cost[ mapping[ "".join( map( str, p ) ) ] ]
if ans >= 10 ** 18:
    print( -1 )
else:
    print( ans )