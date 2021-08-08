N, M, K = map( int, input().split() )
UV = [ tuple( map( int, input().split() ) ) for _ in range( M ) ]
MOD = 998244353

import numpy as np
connect = np.array( [ [ 1 for _ in range( N ) ] for _ in range( N ) ] )
for u, v in UV:
    connect[ u - 1 ][ v - 1 ] = 0
    connect[ v - 1 ][ u - 1 ] = 0

for i in range( N ):
    connect[ i ][ i ] = 0

def mat_power(A,num):
    result=A
    for j in range(num-1):
        result=result.dot(A)
    return np.mod( result, MOD )

A = mat_power( connect, K )
print( A[ 0 ][ 0 ] )