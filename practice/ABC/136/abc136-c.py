N = int( input() )
H = list( map( int, input().split() ) )

highest = -1
for h in H:
    if h < highest - 1:
        print( "No" )
        break
    else:
        highest = max( highest, h )
else:
    print( "Yes" )