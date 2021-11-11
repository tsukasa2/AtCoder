N = int( input() )
L = []
a = []
for _ in range( N ):
    l = list( map( int, input().split() ) )
    L_i = l[ 0 ]
    a_i = l[ 1 : ]
    L.append( L_i )
    a.append( a_i )

s = set()
for a_i in a:
    s.add( " ".join( map( str, a_i ) ) )

print( len( s ) ) 