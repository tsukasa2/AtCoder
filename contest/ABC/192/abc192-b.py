S = str( input() )

for ( i, c ) in enumerate( S ):
    if i % 2 == 0:
        if c.islower() == False:
            print( "No" )
            break
    else:
        if c.islower() == True:
            print( "No" )
            break
else:
    print( "Yes" )