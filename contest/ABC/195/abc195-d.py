import heapq
import copy

N, M, Q = map( int, input().split() )
WV = [ tuple( map( int, input().split() ) ) for _ in range( N ) ]
X = list( map( int, input().split() ) )
Query = [ tuple( map( int, input().split() ) ) for _ in range( Q ) ]

heap = []
for ( w, v ) in WV:
    heapq.heappush( heap, ( -v, w ) )

for ( L, R ) in Query:
    box = []
    for i in range( L - 1 ):
        box.append( X[ i ] )
    
    for i in range( R, M ):
        box.append( X[ i ] )
    # print( box )
    
    box.sort()
    ans = 0
    h = copy.deepcopy( heap )
    for b in box:
        unchosen = []
        while len( h ) > 0:
            v, w = heapq.heappop( h )
            v *= -1
            if w <= b:
                ans += v
                break
            else:
                unchosen.append( ( -v, w ) )
        
        for u in unchosen:
            heapq.heappush( h, u )
    print( ans )