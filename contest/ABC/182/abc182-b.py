N = int( input() )
A = list( map( int, input().split() ) )

gcd_deg = [ 0 for _ in range( 1001 ) ]

for i in range( N ):
    for j in range( 1, A[ i ] + 1 ):
        if A[ i ] % j == 0:
            gcd_deg[ j ] += 1

ans = 0
max_deg = 0
for i in range( 2, 1001 ):
    if gcd_deg[ i ] > max_deg:
        ans = i
        max_deg = gcd_deg[ i ]

print( ans )