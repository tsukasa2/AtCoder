X = str( input() )

if X[ 0 ] == X[ 1 ] and X[ 1 ] == X[ 2 ] and X[ 2 ] == X[ 3 ]:
    print( "Weak" )
else:
    weak = [ "1234", "2345", "3456", "4567", "5678", "6789",
        "7890", "8901", "9012", "0123" ]

    if X in weak:
        print( "Weak" )
    else:
        print( "Strong" )