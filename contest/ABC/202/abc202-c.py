N = int( input() )
A = list( map( int, input().split() ) )
B = list( map( int, input().split() ) )
C = list( map( int, input().split() ) )

from collections import Counter
count = Counter()


for j in range( N ):
    count[ B[ C[ j ] - 1 ] ] += 1

ans = 0
for i in range( N ):
    ans += count[ A[ i ] ]

print( ans )