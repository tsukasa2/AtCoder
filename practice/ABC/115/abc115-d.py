import sys
sys.setrecursionlimit( 10 ** 8 )

N, X = map( int, input().split() )

patty = [ 1 ]
tot = [ 1 ]
for _ in range( 50 ):
    patty.append( 2 * patty[ -1 ] + 1 )
    tot.append( 2 * tot[ -1 ] + 3 )

def f( level, x ):
    # f( level, x ) = レベルlevelバーガーの層x以下にあるパティの枚数
    if level == 0:
        return 1
    else:
        if x == 0:
            return 0
        elif x <= tot[ level - 1 ]:
            return f( level - 1, x - 1 )
        elif x == tot[ level - 1 ] + 1:
            return patty[ level - 1 ] + 1
        elif x <= 2 * tot[ level - 1 ] + 1:
            return patty[ level - 1 ] + 1 + f( level - 1, x - ( tot[ level - 1 ] + 2 ) )
        else:
            return patty[ level ]

print( f( N, X - 1 ) )