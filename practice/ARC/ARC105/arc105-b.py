N = int( input() )
a = list( map( int, input().split() ) )

# import heapq
# heap_a = []
# min_a = a[ 0 ]
# for i in range( N ):
#     heapq.heappush( heap_a, a[ i ] * ( -1 ) )
#     if a[ i ] < min_a:
#         min_a = a[ i ]

# while True:
#     max_a = heapq.heappop( heap_a ) * ( -1 )

#     if max_a - min_a == 0:
#         print( min_a )
#         break
    
#     heapq.heappush( heap_a, ( max_a - min_a ) * ( -1 ) )
    
#     if max_a - min_a < min_a:
#         min_a = max_a - min_a

import math
ans = a[ 0 ]
for i in range( N ):
    ans = math.gcd( ans, a[ i ] )
print( ans )