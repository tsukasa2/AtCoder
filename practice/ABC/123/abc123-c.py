N = int( input() )
capacity = [ int( input() ) for _ in range( 5 ) ]

import math

delay = [ 0 ] * 5
delay[ 0 ] = math.ceil( N / capacity[ 0 ] )

for i in range( 1, 5 ):
    delay[ i ] = max( delay[ i - 1 ] + 1, i + math.ceil( N / capacity[ i ] ) )

# print( delay )
print( delay[ -1 ] )