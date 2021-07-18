N, K = map( int, input().split() )
c = list( map( int, input().split() ) )

from collections import Counter
count = Counter()

ans = 0
for c_i in c[ : K ]:
    count[ c_i ] += 1
    if count[ c_i ] == 1:
        ans += 1

ans_max = ans
for i, c_i in enumerate( c[ K : ] ):
    count[ c[ i ] ] -= 1
    if count[ c[ i ] ] == 0:
        ans -= 1
    
    count[ c_i ] += 1
    if count[ c_i ] == 1:
        ans += 1
    
    ans_max = max( ans_max, ans )

print( ans_max )