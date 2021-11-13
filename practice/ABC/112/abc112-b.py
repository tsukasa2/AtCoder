N, T = map( int, input().split() )
ct = [ tuple( map( int, input().split() ) ) for _ in range( N ) ]

c_cand = []
for c, t in ct:
    if t <= T:
        c_cand.append( c )

if c_cand:
    print( min( c_cand ) )
else:
    print( "TLE" )