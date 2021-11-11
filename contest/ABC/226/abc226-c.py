import sys
sys.setrecursionlimit( 10 ** 8 )

N = int( input() )
TKA = [ tuple( map( int, input().split() ) ) for _ in range( N ) ]

moves = set()

def solve( n ):
    moves.add( n )
    n -= 1
    T, K, A = TKA[ n ][ 0 ], TKA[ n ][ 1 ], TKA[ n ][ 2 : ]
    if K > 0:
        for a in A:
            if not a in moves:
                solve( a )

solve( N )
ans = 0
for n in moves:
    ans += TKA[ n - 1 ][ 0 ]

print( ans )