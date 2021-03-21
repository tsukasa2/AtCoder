import sys
sys.setrecursionlimit(200100)
n, m, k = map( int, input().split() )
friend = [ [] for _ in range( n ) ]

for _ in range( m ):
    a, b = map( int, input().split() )
    friend[ a - 1 ].append( b - 1 )
    friend[ b - 1 ].append( a - 1 )

graph_id = [ -1 for _ in range( n ) ]

def dfs( ver, g_id ):
    if graph_id[ ver ] == -1:
        graph_id[ ver ] = g_id
    else:
        return
    for next_v in friend[ ver ]:
        dfs( next_v, g_id )

g_id = 0
for ver in range( n ):
    if graph_id[ ver ] != -1:
        continue
    dfs( ver, g_id )
    g_id += 1

graph_size = [ 0 for _ in range( n ) ]
for ver in range( n ):
    graph_size[ graph_id[ ver ] ] += 1

ans = [ graph_size[ graph_id[ ver ] ] for ver in range( n ) ]

for _ in range( k ):
    c, d = map( int, input().split() )
    if graph_id[ c - 1 ] == graph_id[ d - 1 ]:
        ans[ c - 1 ] -= 1
        ans[ d - 1 ] -= 1

for ver in range( n ):
    ans[ ver ] = ans[ ver ] - len( friend[ ver ] ) - 1

print( " ".join( map( str, ans ) ) )