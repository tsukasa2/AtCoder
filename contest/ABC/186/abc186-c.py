N = int( input() )

count = 0
for k in range( 1, N + 1 ):
    if "7" in str( k ):
        count += 1
    elif "7" in oct( k ):
        count += 1

print( N - count )