N = int( input() )

ans = 0
for A in range( 1, int( N ** ( 1 / 3 ) ) + 10 ):
    for B in range( A, int( ( N / A ) ** 0.5 ) + 10 ):
        C_max = N // ( A * B )
        if C_max >= B and B >= A:
            ans += C_max - B + 1

print( ans )