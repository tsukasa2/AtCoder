K = int( input() )

ans = 0
for A in range( 1, K + 1 ):
    for B in range( 1, K // A + 1 ):
        ans += K // ( A * B )

print( ans )