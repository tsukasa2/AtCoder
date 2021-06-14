N = int( input() )
A = list( map( int, input().split() ) )

A.sort()
for i, a in enumerate( A ):
    if not i + 1 == a:
        print( "No" )
        break
else:
    print( "Yes" )