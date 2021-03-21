import math


N = int( input() )
H = list( map( int, input().split() ) )

max_count = -1
count = 0
for i in range( N ):
    if i < N - 1:
        if H[ i ] >= H[ i + 1 ]:
            count += 1
        else:
            max_count = max( max_count, count )
            count = 0
    else:
        max_count = max( max_count, count )
        count = 0

print( max_count )