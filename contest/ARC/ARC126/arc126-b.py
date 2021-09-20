from bisect import bisect_left, insort_left
import array

N, M = map( int, input().split() )
ab = [ tuple( map( int, input().split() ) ) for _ in range( M ) ]

ab.sort()
bs = {}
for ( a, b ) in ab:
    try:
        bs[ a ].append( b )
    except KeyError:
        bs[ a ] = [ b ]

edges = [ ( a, bs[ a ] ) for a in bs.keys() ]
edges.sort()

INF = 2 * 10 ** 5 + 100
lst = [ INF ] * ( M + 1 )

for i, ( a, b_list ) in enumerate( edges ):
    b_list.sort( reverse = True )
    j_list = []
    for b in b_list:
        j = bisect_left( lst, b )
        j_list.append( j )
    
    for k in range( len( b_list ) ):
        lst[ j_list[ k ] ] = b_list[ k ]

# print( lst )
ans = 0
for i, t in enumerate( lst ):
    x = t
    if x == INF:
        print( ans )
        break
    else:
        ans = i + 1
else:
    print( ans )