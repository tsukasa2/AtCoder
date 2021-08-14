import sys
sys.setrecursionlimit( 10 ** 6 )

N = int( input() )
AB = [ tuple( map( int, input().split() ) ) for _ in range( N - 1 ) ]

connect = [ [] for _ in range( N ) ]
for ( a, b ) in AB:
    connect[ a - 1 ].append( b - 1 )
    connect[ b - 1 ].append( a - 1 )

for i in range( N ):
    connect[ i ] = sorted( connect[ i ] )

visited = [ False for _ in range( N ) ]
ans = []
def dfs( v ):
    visited[ v ] = True
    ans.append( v + 1 )
    for u in connect[ v ]:
        if not visited[ u ]:
            dfs( u )
            ans.append( v + 1 )

dfs( 0 )
print( " ".join( map( str, ans ) ) )