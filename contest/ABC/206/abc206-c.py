N = int( input() )
A = list( map( int, input().split() ) )

from collections import Counter
count = Counter()

for a in A:
    count[ a ] += 1

ans = 0
used = 0
for a in count.keys():
    c = count[ a ]
    ans += c * ( N - used - c )
    used += c

print( ans )