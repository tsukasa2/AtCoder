x, n = map( int, input().split() )
p = list( map( int, input().split() ) )

for i in range( n + 1 ):
    if ( x - i ) not in p:
        print( x - i )
        break
    elif ( x + i ) not in p:
        print( x + i )
        break