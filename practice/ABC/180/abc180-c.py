N = int( input() )

ans = []
for i in range( 1, int( pow( N, 1/2 ) + 1 ) ):
    if N % i == 0:
        ans.append( i )
        if N != i ** 2:
            ans.append( N // i )

for a in sorted( ans ):
    print( a )