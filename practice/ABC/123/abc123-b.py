Time = [ int( input() ) for _ in range( 5 ) ]

import math
Time_10 = [ math.ceil( t / 10 ) * 10 for t in Time ]
Time_1 = []
for t in Time:
    if not t % 10 == 0:
        Time_1.append( t % 10 )

if not Time_1:
    Time_1.append( 10 )

print( sum( Time_10 ) - ( 10 - min( Time_1 ) ) )