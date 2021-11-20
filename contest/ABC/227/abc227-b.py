from collections import Counter

N = int( input() )
S = list( map( int, input().split() ) )

count = Counter()
for a in range( 1, 150 ):
    for b in range( 1, 150 ):
        count[ 4 * a * b + 3 * a + 3 * b ] += 1

ans = 0
for s in S:
    if count[ s ] == 0:
        ans += 1

print( ans )