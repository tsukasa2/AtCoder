N = int( input() )

import itertools
from bisect import bisect_right, insort_right
import array

lst = array.array( "l", [] )
for i in range( 3, 10 ):
    for c in itertools.product( [ "7", "5", "3" ], repeat = i ):
        if "7" in c and "5" in c and "3" in c:
            x = int( "".join( c ) )
            insort_right( lst, x )

print( bisect_right( lst, N ) )