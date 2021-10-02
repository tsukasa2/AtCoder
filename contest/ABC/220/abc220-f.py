import sys
sys.setrecursionlimit( 10 ** 8 )

N = int( input() )
uv = [ tuple( map( int, input().split() ) ) for _ in range( N - 1 ) ]

connect = [ [] for _ in range( N ) ]
for u, v in uv:
    connect[ u - 1 ].append( v - 1 )
    connect[ v - 1 ].append( u - 1 )

size = [ 0 for _ in range( N ) ]
# size[ u ] = 頂点uを根とする部分木の頂点数
visited = [ False ] * N
depth = [ 0 ] * N

def calc_size( v ):
    # 頂点vを根とする部分木の頂点数を計算
    size[ v ] += 1
    visited[ v ] = True
    for u in connect[ v ]:
        if visited[ u ] == False:
            depth[ u ] = depth[ v ] + 1
            calc_size( u )
            size[ v ] += size[ u ]

calc_size( 0 )
# print( size, depth )

ans = [ sum( depth ) ] + [ -1 ] * ( N - 1 )
# ans[ i ] = i行目の答え

from collections import deque
queue = deque( [ 0 ] )
while queue:
    v = queue.popleft()
    ans_v = ans[ v ]
    for u in connect[ v ]:
        if ans[ u ] == -1:
            ans[ u ] = ans_v - size[ u ] + ( N - size[ u ] )
            # 根をvからuに変えると，uの部分木に含まれる頂点は根からの距離が1減り，
            # それ以外の頂点は根からの距離が1増える
            
            queue.append( u )

print( *ans, sep = "\n" )