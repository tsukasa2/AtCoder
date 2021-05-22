N = int( input() )
A = list( map( int, input().split() ) )

S = [ 0 ]
for ( i, a ) in enumerate( A ):
    if i % 2 == 0:
        S.append( S[ -1 ] + a )
    else:
        S.append( S[ -1 ] - a )

from collections import Counter
count = Counter()

for s in S:
    count[ s ] += 1

ans = 0
for c in count.values():
    ans += c * ( c - 1 ) // 2

print( ans )