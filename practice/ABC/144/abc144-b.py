N = int( input() )

for A in range( 1, 10 ):
    if N % A == 0:
        B = N // A
        if B < 10:
            print( "Yes" )
            break
else:
    print( "No" )