# ABC198 E

from collections import Counter
import sys
sys.setrecursionlimit( 10 ** 6 )

N = int( input() )
C = list( map( int, input().split() ) )
AB = [ tuple( map( int, input().split() ) ) for _ in range( N - 1 ) ]

connect = [ [] for _ in range( N ) ]
for ( a, b ) in AB:
    connect[ a - 1 ].append( b - 1 )
    connect[ b - 1 ].append( a - 1 )

visited = [ False for _ in range( N ) ]
found = Counter()
ans = []

def dfs( v ):
    visited[ v ] = True
    c = C[ v ]
    if found[ c ] == 0:
        ans.append( v + 1 )
    
    found[ c ] += 1
    for u in connect[ v ]:
        if visited[ u ] == False:
            dfs( u )
    found[ c ] -= 1

dfs( 0 )

ans.sort()
print( *ans, sep="\n" )