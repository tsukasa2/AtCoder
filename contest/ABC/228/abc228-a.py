S, T, X = map( int, input().split() )

if S < T:
    if S <= X and X < T:
        print( "Yes" )
    else:
        print( "No" )
else:
    if S <= X:
        print( "Yes" )
    elif X < T:
        print( "Yes" )
    else:
        print( "No" )