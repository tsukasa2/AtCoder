n = int( input() )
s = []
for i in range( n ):
    s.append( input() )

#print( s )

kind = {}

for i in range( n ):
    try:
        kind[ s[i] ] += 1
    except KeyError:
        kind[ s[i] ] = 0

print( len( kind.keys() ) )