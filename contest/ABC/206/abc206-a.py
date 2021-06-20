N = int( input() )

import math

N = math.floor( N * 1.08 )

if N < 206:
    print( "Yay!" )
elif N == 206:
    print( "so-so" )
else:
    print( ":(" )