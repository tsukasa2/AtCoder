N, M = map( int, input().split() )
AB = [ [] for _ in range( M + 1 ) ]
# AB[ i ] = i日後に報酬をもらえるバイトのリスト
for _ in range( N ):
    a, b = map( int, input().split() )
    if a < M + 1:
        AB[ a ].append( b )

from heapq import heappush, heappop
ab_heap = []
ans = 0
for i in range( M ):
    # ( M - 1 - i )日目にするバイトを考える
    for b in AB[ i + 1 ]:
        heappush( ab_heap, -b )

    if ab_heap:
        ans += -heappop( ab_heap )

print( ans )