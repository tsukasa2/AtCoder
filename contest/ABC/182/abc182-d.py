N = int( input() )
A = list( map( int, input().split() ) )

max_ad = 0
sum_A = 0
max_x = A[ 0 ]
now_x = 0
for i in range( N ):
    if sum_A + A[ i ] > max_ad:
        max_ad = sum_A + A[ i ]
    sum_A += A[ i ]
    if now_x + max_ad > max_x:
        max_x = now_x + max_ad
    now_x += sum_A
    # print( A[ i ], max_x, now_x )

print( max_x )