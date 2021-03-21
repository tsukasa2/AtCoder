n = int( input() )
a = list( map( int, input().split() ) )

cnt = {}

for a_i in a:
    try:
        cnt[ a_i ]
        print( "NO" )
        break
    except KeyError:
        cnt[ a_i ] = 1
else:
    print( "YES" )