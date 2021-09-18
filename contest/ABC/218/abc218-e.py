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
ABC = [ tuple( map( int, input().split() ) ) for _ in range( M ) ]

edge = []
ans = 0
for a, b, c in ABC:
    edge.append( ( c, a - 1, b - 1 ) )
    ans += c

edge.sort()
# print( edge )

tree = UnionFind( N )
for c, a, b in edge:
    if tree.same( a, b ) == True:
        if c < 0:
            ans -= c
            
        continue
    
    tree.union( a, b )
    ans -= c

print( ans )