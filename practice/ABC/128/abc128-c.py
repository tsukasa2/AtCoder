N, M = map( int, input().split() )
k = []
s = []
for _ in range( M ):
    tmp = list( map( int, input().split() ) )
    k.append( tmp[ 0 ] )
    s.append( tmp[ 1 : ] )

p = list( map( int, input().split() ) )

from itertools import chain,combinations
def powerset(iterable):
    "powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

ans = 0
for pw in powerset( [ i + 1 for i in range( N ) ] ):
    switches = [ 0 for _ in range( M ) ]
    lamps = [ 0 for _ in range( M ) ]
    for i in range( M ):
        for j in range( k[ i ] ):
            if s[ i ][ j ] in pw:
                switches[ i ] += 1
        
        if switches[ i ] % 2 == p[ i ]:
            lamps[ i ] = 1
    
    if sum( lamps ) == M:
        ans += 1

print( ans )