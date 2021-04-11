T = int( input() )
case = [ int( input() ) for _ in range( T ) ]

for c in case:
    if c % 4 == 0:
        print( "Even" )
    elif c % 2 == 0:
        print( "Same" )
    else:
        print( "Odd" )