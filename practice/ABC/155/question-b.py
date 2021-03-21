n = int( input() )
a = list( map( int, input().split() ) )

for x in a:
    if x % 2 == 0:
        if x % 3 == 0:
            continue
        if x % 5 == 0:
            continue
        print( "DENIED" )
        break
else:
    print( "APPROVED" )