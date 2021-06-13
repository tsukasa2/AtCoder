N, K = map( int, input().split() )
A = list( map( int, input().split() ) )

import math

L = 0
R = 10 ** 9 + 1000
while R - L > 1:
    M = ( L + R ) // 2
    k = 0
    for a in A:
        k += math.ceil( a / M ) - 1
    
    if k > K:
        L = M
    else:
        R = M

print( R )