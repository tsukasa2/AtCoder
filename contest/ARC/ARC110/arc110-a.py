import math

N = int( input() )

ans = 1
for k in range( 2, N + 1 ):
    ans = ans * k // math.gcd( ans, k )

print( ans + 1 )