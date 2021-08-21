N = int( input() )
uvw = [ tuple( map( int, input().split() ) ) for _ in range( N - 1 ) ]

# connect = [ [] for _ in range( N ) ]
# for u, v, w in uvw:
#     connect[ u - 1 ].append( ( v - 1, w ) )
#     connect[ v - 1 ].append( ( u - 1, w ) )

# from collections import deque
# depth = [ -1 ] * N
# depth[ 0 ] = 0
# queue = deque( [ 0 ] )
# leaves = []
# parent = [ -1 ] * N
# while queue:
#     v = queue.popleft()

#     leave = True
#     for u, _ in connect[ v ]:
#         if depth[ u ] >= 0:
#             continue     
#         else:
#             depth[ u ] = depth[ v ] + 1
#             queue.append( u )
#             parent[ u ] = v
#             leave = False
    
#     if leave:
#         leaves.append( v )

# sorted_nodes = sorted( [ ( -d, i ) for i, d in enumerate( depth ) ] )
# nums_of_nodes = [ 1 ] * N
# for _, v in sorted_nodes:
#     if v == 0:
#         continue

#     p = parent[ v ]
#     nums_of_nodes[ p ] += nums_of_nodes[ v ]

# rest_of_nodes = [ N + 1 - num for num in nums_of_nodes ]
# sorted_uvw = sorted( [ ( -w, u, v, w ) for u, v, w in uvw ] )
# ans = 0
# for _, u, v, w in sorted_uvw:
#     u, v = u - 1, v - 1
#     if depth[ u ] > depth[ v ]:
#         u, v = v, u
    
#     pairs = nums_of_nodes[ v ] * rest_of_nodes[ u ]
#     ans += w * pairs

class UnionFind():
    def __init__( self, N ):
        self.par = [ i for i in range( N ) ]
        # self.par[ x ] = xの親．初期値は自分自身
        self.dim = [ 1 for _ in range( N ) ]
        # self.dim[ x ] = xを根とする木の要素数

    def root( self, x ):
        if self.par[ x ] == x:
            return x
        else:
            self.par[ x ] = self.root( self.par[ x ] )
            # xの親の根をxの親とする
            return self.par[ x ]
    
    def union( self, x, y ):
        rx = self.root( x )
        ry = self.root( y )
        if rx == ry:
            # xとyがもともと同じ木にいた場合はパス
            return False
        else:
            # 小さい木を大きい木に吸収させる
            if self.size( rx ) < self.size( ry ):
                rx, ry = ry, rx
            self.dim[ rx ] += self.dim[ ry ]
            self.par[ ry ] = rx
            return True

    def same( self, x, y ):
        rx = self.root( x )
        ry = self.root( y )
        if rx == ry:
            return True
        else:
            return False
    
    def size( self, x ):
        return self.dim[ self.root( x ) ]

tree = UnionFind( N )
sorted_uvw = sorted( [ ( w, u, v, w ) for u, v, w in uvw ] )
ans = 0
for _ , u, v, w in sorted_uvw:
    u -= 1
    v -= 1
    ans += w * tree.size( u ) * tree.size( v )
    tree.union( u, v )

print( ans )