H, W, A, B = map( int, input().split() )

ans = 0

primes = [ 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53 ]

import copy

def solve( x, visited, A, B ):
    global ans

    if x == H * W - 1:
        ans += 1
        return

    if visited % primes[ x ] == 0:
        solve( x + 1, visited, A, B )
        return

    if A > 0:
        if x % W < W - 1:
            if visited % primes[ x + 1 ] > 0:
                solve( x + 1, visited * primes[ x ] * primes[ x + 1 ], A - 1, B )
        if x // W < H - 1:
            if visited % primes[ x + W ] > 0:
                solve( x + 1, visited * primes[ x ] * primes[ x + W ], A - 1, B )

    if B > 0:
        solve( x + 1, visited * primes[ x ], A, B - 1 )

solve( 0, 1, A, B )
print( ans )
