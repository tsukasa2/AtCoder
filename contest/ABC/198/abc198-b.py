N = str( input() )

while True:
    if N == N[ : : -1 ]:
        print( "Yes" )
        break
    else:
        if N[ -1 ] == "0":
            N = N[ : -1 ]
        else:
            print( "No" )
            break