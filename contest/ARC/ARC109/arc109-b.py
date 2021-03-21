import math

n = int( input() )

root_n = int( math.sqrt( 2 * n ) )
k = root_n

while k * ( k + 3 ) > 2 * n:
    k = k - 1

print( n - k )