A, B, C, D = map( int, input().split() )

import math

if C * D - B > 0:
    print( math.ceil( A / ( C * D - B ) ) )
else:
    print( -1 )