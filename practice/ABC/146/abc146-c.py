A, B, X = map( int, input().split() )

import math
def d( n ):
    if n > 0:
        return math.floor( math.log10( n ) ) + 1
    else:
        return 0

# ans = 10 ** 9
# if A * ans + B * d( ans ) > X:
#     ans = X // A
#     while A * ans + B * d( ans ) > X:
#         ans = ans - 1

# print( ans )

def f( n ):
    return A * n + B * d( n )

l, r = 0, 10 ** 9 + 1
while r - l > 1:
    m = ( l + r ) // 2
    if f( m ) > X:
        r = m
    else:
        l = m

print( l )