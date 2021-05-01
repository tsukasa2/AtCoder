N = int( input() )
SP = []
for _ in range( N ):
    s, p = input().split()
    s = str( s )
    p = int( p )
    SP.append( ( s, p ) )

shi = []
mise = {}
for i, ( s, p ) in enumerate( SP ):
    try:
        mise[ s ].append( ( p, i ) )
    except KeyError:
        mise[ s ] = [ ( p, i ) ]
        shi.append( s )

shi.sort()
for s in shi:
    mise[ s ].sort( reverse = True )
    for ( _, i ) in mise[ s ]:
        print( i + 1 )