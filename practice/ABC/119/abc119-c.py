N, A, B, C = map( int, input().split() )
l = [ int( input() ) for _ in range( N ) ]

import sys
sys.setrecursionlimit( 10 ** 8 )

def solve( n, a = 0, b = 0, c = 0, mp = 0 ):
    if n <= 0:
        if a == 0 or b == 0 or c == 0:
            return 10 ** 12

        return abs( A - a ) + abs( B - b ) + abs( C - c ) + mp
    else:
        l_i = l[ -n ]
        if a == 0:
            res_a = solve( n - 1, a + l_i, b, c, mp )
        else:
            res_a = solve( n - 1, a + l_i, b, c, mp + 10 )

        if b == 0:
            res_b = solve( n - 1, a, b + l_i, c, mp )
        else:
            res_b = solve( n - 1, a, b + l_i, c, mp + 10 )
        
        if c == 0:
            res_c = solve( n - 1, a, b, c + l_i, mp )
        else:
            res_c = solve( n - 1, a, b, c + l_i, mp + 10 )
        
        res_d = solve( n - 1, a, b, c, mp )

        return min( [ res_a, res_b, res_c, res_d ] )

print( solve( N ) )