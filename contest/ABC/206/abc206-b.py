N = int( input() )

import math
i = math.floor( ( 2 * N ) ** 0.5 )

while i * ( i + 1 ) < 2 * N:
    i += 1

print( i )