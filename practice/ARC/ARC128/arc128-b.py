INF = 10 ** 18

T = int( input() )
cases = [ tuple( map( int, input().split() ) ) for _ in range( T ) ]

def solve( R, G, B ):
    # すべてをRに変えることができるかを調べる
    # Gの数 == Bの数 にすることができればいい
    if G > B:
        G, B = B, G
    
    if ( B - G ) % 3 > 0:
        return INF
    else:
        return ( B - G ) // 3 + ( 2 * B + G ) // 3

for case in cases:
    R, G, B = case
    ans = min(
        [
            solve( R, G, B ),
            solve( G, B, R ),
            solve( B, R, G )
        ]
    )
    if ans == INF:
        print( -1 )
    else:
        print( ans )