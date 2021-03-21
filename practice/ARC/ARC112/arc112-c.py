# ARC112 C
n = int( input() )
p = list( map( int, input().split() ) )

p = [ -1 ] + p
child = [ [] for _ in range( n ) ]
for i in range( 1, n ):
    p[ i ] -= 1
    child[ p[ i ] ].append( i )

f = [ 0 for _ in range( n ) ]
# f[ u ] = 頂点uを根とする部分木からスタートしたときの
# 後手のコイン数 - 先手のコイン数

size = [ 0 for _ in range( n ) ]
# size[ u ] = 頂点uを根とする部分木の頂点数

def calc_size( v ):
    # 頂点vを根とする部分木の頂点数を計算
    size[ v ] += 1
    for u in child[ v ]:
        calc_size( u )
        size[ v ] += size[ u ]

calc_size( 0 )
print( "size: ", size )

from heapq import heappop, heappush
def calc_f( v ):
    # f( v )を計算
    if not child[ v ]:
        return -1
    else:
        heap = []
        for u in child[ v ]:
            f_u = calc_f( u )
            case_u = 1
            # めんどいからやめた
