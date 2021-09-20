from bisect import bisect_left

def LIS( seq ):
    INF = 10 ** 12
    DP = [ INF ] * ( len( seq ) + 1 )
    res = 1
    for s in seq:
        i = bisect_left( DP, s )
        if DP[ i ] == INF:
            res = i + 1

        DP[ i ] = s
    
    return res

import random
ary = [ random.randint( 1, 100 ) for _ in range( 10 ) ]
print( ary )
print( LIS( ary ) )