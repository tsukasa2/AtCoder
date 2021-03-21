import itertools
import math

N = int( input() )
town = []
for _ in range( N ):
    x, y = map( int, input().split() )
    town.append( ( x, y ) )

def distance( town1, town2 ):
    x1 = town1[ 0 ]
    y1 = town1[ 1 ]
    x2 = town2[ 0 ]
    y2 = town2[ 1 ]
    return math.sqrt( ( ( x1 - x2 ) ** 2 ) + ( ( y1 - y2 ) ** 2 ) )

sum_d = 0
for p in itertools.permutations( town, N ):
    d = 0
    for i in range( 1, N ):
        town1 = p[ i - 1 ]
        town2 = p[ i ]
        d += distance( town1, town2 )
    sum_d += d

print( sum_d / math.factorial( N ) )
