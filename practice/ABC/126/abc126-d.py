import sys
sys.setrecursionlimit( 10 ** 9 )

N = int( input() )
EDGE = [ tuple( map( int, input().split() ) ) for _ in range( N - 1 ) ]

connect = [ [] for _ in range( N ) ]
for u, v, w in EDGE:
    u = u - 1
    v = v - 1
    connect[ u ].append( ( v, w ) )
    connect[ v ].append( ( u, w ) )

depth = [ float( "inf" ) for _ in range( N ) ]
depth[ 0 ] = 0

def dfs( v ):
    for u, w in connect[ v ]:
        if depth[ u ] == float( "inf" ):
            depth[ u ] = depth[ v ] + w
            dfs( u )

dfs( 0 )

color = [ 0 for _ in range( N ) ]
for i, d in enumerate( depth ):
    if d % 2 == 0:
        color[ i ] = 1

for c in color:
    print( c )