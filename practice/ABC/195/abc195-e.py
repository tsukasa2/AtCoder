N = int( input() )
S = str( input() )
X = str( input() )

DP = [ set() for _ in range( N + 1 ) ]
# DP[ i ] = { r | iラウンド終了した時点で余りがrなら高橋くんに勝ち目がある }

DP[ N ].add( 0 )
for i in reversed( range( 1, N + 1 ) ):
    if X[ i - 1 ] == "T":
        for r in range( 7 ):
            if 10 * r % 7 in DP[ i ]:
                DP[ i - 1 ].add( r )
            elif ( 10 * r + int( S[ i - 1 ] ) ) % 7 in DP[ i ]:
                DP[ i - 1 ].add( r )
    else:
        for r in range( 7 ):
            if 10 * r % 7 in DP[ i ]:
                if ( 10 * r + int( S[ i - 1 ] ) ) % 7 in DP[ i ]:
                    DP[ i - 1 ].add( r )

if 0 in DP[ 0 ]:
    print( "Takahashi" )
else:
    print( "Aoki" )