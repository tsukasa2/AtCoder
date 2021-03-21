import math

N = int( input() )

root_N = int( math.sqrt( N ) )

i, j = 1, 1
for k in range( 1, root_N + 1 ):
    if N % k == 0:
        i = k
        j = N // k

print( i + j - 2 )