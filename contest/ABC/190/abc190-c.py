N, M = map( int, input().split() )
AB = [ tuple( map( int, input().split() ) ) for _ in range( M ) ]
K = int( input() )
CD = [ tuple( map( int, input().split() ) ) for _ in range( K ) ]

import sys
sys.setrecursionlimit( 10 ** 8 )
import copy

dish = []

def search( k = 0, on = set() ):
    if k == K:
        dish.append( on )
        return True
    c, d = CD[ k ]
    on1 = copy.deepcopy( on )
    on2 = copy.deepcopy( on )
    on1.add( c )
    on2.add( d )
    search( k + 1, on1 )
    search( k + 1, on2 )

search()

answer = -1
for d in dish:
    ans = 0
    for ( a, b ) in AB:
        if a in d and b in d:
            ans += 1
    answer = max( ans, answer )

print( answer )