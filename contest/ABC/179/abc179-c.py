n = int( input() )

s = 0
for k in range( 1, n ):
    s = s + ( ( n - 1 ) // k )

print( s )