N = int( input() )
ST = [ tuple( map( str, input().split() ) ) for _ in range( N ) ]

mountains = []
for ( S, T ) in ST:
    mountains.append( ( int( T ), S ) )

mountains.sort()
print( mountains[ -2 ][ 1 ] )