N, M, X, Y = map( int, input().split() )
X -= 1
Y -= 1
ABTK = [ tuple( map( int, input().split() ) ) for _ in range( M ) ]

train = [ [] for _ in range( N ) ]
for ( a, b, t, k ) in ABTK:
    a -= 1
    b -= 1
    train[ a ].append( ( b, t, k ) )
    train[ b ].append( ( a, t, k ) )

def wait( now, k ):
    return ( k - now % k ) % k

from heapq import heappop, heappush
INF = 10 ** 18
cost = [ INF for _ in range( N ) ]
cost[ X ] = 0
visited = [ False for _ in range( N ) ]
queue = [ ( cost[ X ], X ) ]
while queue:
    c, v = heappop( queue )
    visited[ v ] = True
    for u, t, k in train[ v ]:
        if visited[ u ] == True:
            continue
        else:
            if cost[ u ] > c + t + wait( c, k ):
                cost[ u ] = c + t + wait( c, k )
                heappush( queue, ( cost[ u ], u ) )

if cost[ Y ] >= INF:
    print( -1 )
else:
    print( cost[ Y ] )