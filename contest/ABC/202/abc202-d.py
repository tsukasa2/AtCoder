A, B, K = map( int, input().split() )

import math
def comb( x, y ):
    return math.factorial( x + y ) // math.factorial( x ) // math.factorial( y )

k = 0
ans = ""
while A > 0 and B > 0:
    c = comb( A - 1, B )
    if k + c < K:
        ans += "b"
        B -= 1
        k += c
    else:
        ans += "a"
        A -= 1

ans = ans + "a" * A + "b" * B

print( ans )    