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

N, M = map( int, input().split() )
UV = [ tuple( map( int, input().split() ) ) for  _ in range( M ) ]

MOD = 998244353

dims = [ 0 ] * N
tree = UnionFind( N )
for u, v in UV:
    tree.union( u - 1, v - 1 )
    dims[ u - 1 ] += 1
    dims[ v - 1 ] += 1

edges = [ 0 ] * N
for x in range( N ):
    edges[ tree.root( x ) ] += dims[ x ]

parents = []
for x in range( N ):
    if tree.root( x ) == x:
        parents.append( x )

ans = 1
for p in parents:
    if edges[ p ] == 2 * tree.size( p ):
        ans *= 2
        ans %= MOD
    else:
        ans *= 0

print( ans )