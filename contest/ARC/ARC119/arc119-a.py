N = int( input() )

ans = 3 * ( 10 ** 18 )
pow_2_b = 1
for b in range( 61 ):
    a = N // pow_2_b
    c = N % pow_2_b
    ans = min( ans, a + b + c )
    pow_2_b *= 2

print( ans )