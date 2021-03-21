N = int( input() )
A = list( map( int, input().split() ) )

import math
def lcm( n, m ):
    return n * m // math.gcd( n, m )

LCM_A = 1
for a in A:
    LCM_A = lcm( LCM_A, a )

bumbo = 0
for a in A:
    bumbo += LCM_A // a

print( LCM_A / bumbo )