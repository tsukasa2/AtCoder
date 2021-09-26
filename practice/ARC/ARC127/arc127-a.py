N = int( input() )

ans = 0
for i in range( 1, 17 ):
    for j in range( 0, 17 - i ):
        y = int( "1" * i + "9" * j )
        z = int( "1" * i + "0" * j ) - 1
        if N >= y:
            ans += 10 ** j
        else:
            ans += max( 0, N - z )
        
        # print( y, z,  ans )

print( ans )