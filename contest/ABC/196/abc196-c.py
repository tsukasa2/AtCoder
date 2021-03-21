N = int( input() )

ans = 0

for k in range( 1, 10 ** 6 + 100 ):
    doubled_k = int( str( k ) + str( k ) )
    if doubled_k > N:
        print( ans )
        break
    ans += 1