A, B, C, D = map( int, input().split() )

import math
l = C * D // math.gcd( C, D )

ans = B - ( A - 1 )

ans -= B // C - ( A - 1 ) // C
ans -= B // D - ( A - 1 ) // D
ans += B // l - ( A - 1 ) // l

print( ans )