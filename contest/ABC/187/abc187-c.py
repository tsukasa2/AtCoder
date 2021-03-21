N = int( input() )
S = []
for _ in range( N ):
    s = str( input() )
    S.append( s )

found = {}
for s in S:
    found[ s ] = "Found"

for s in S:
    try:
        if found[ "!" + s ]:
            print( s )
            break
    except KeyError:
        continue
else:
    print( "satisfiable" )