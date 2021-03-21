x = int( input() )

for a in range( 10001 ):
    for b in range( a + 1 ):
        if a ** 5 + b ** 5 == x:
            print( str( a ) + " " + str( -b ) )
            exit()
        elif a ** 5 - b ** 5 == x:
            print( str( a ) + " " + str( b ) )
            exit()