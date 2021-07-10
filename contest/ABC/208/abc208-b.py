P = int( input() )

coins = [ 1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880, 3628800 ]

ans = 0
for i in reversed( range( 1, 11 ) ):
    c = coins[ i ]
    ans += P // c
    P = P % c

print( ans )