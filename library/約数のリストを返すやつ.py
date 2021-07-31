# ARC124 C

N = int( input() )
ab = [ tuple( map( int, input().split() ) ) for _ in range( N ) ]

LCMs = []
def make_divisors( n ):
    lower_divisors, upper_divisors = [], []
    i = 1
    while i * i <= n:
        if n % i == 0:
            lower_divisors.append( i )
            if i != n // i:
                upper_divisors.append( n // i )
        i += 1
    return lower_divisors + upper_divisors[ ::-1 ]

import math
for X in make_divisors( ab[ 0 ][ 0 ] ):
    for Y in make_divisors( ab[ 0 ][ 1 ] ):
        for i in range( N ):
            a, b = ab[ i ]
            if a % X == 0 and b % Y == 0:
                continue
            elif b % X == 0 and a % Y == 0:
                continue
            
            break
        else:
            LCMs.append( X * Y // math.gcd( X, Y ) )

print( max( LCMs ) )