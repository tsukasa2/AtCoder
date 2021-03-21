N = int( input() )
ab = []
for _ in range( N ):
    a, b = map( int, input().split() )
    ab.append( ( a - 1, b - 1 ) )

class UnionFind():
    def __init__( self, N ):
        self.par = [ i for i in range( N ) ]
        # self.par[ x ] = xの親．初期値は自分自身
        self.dim = [ 1 for _ in range( N ) ]
        # self.dim[ x ] = xを根とする木の要素数
        self.edge = [ 0 for _ in range( N ) ]
        # self.edge[ x ] = xを根とする木の辺の数

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
            self.edge[ rx ] += 1
        if rx == ry:
            # xとyがもともと同じ木にいた場合はパス
            return False
        else:
            # 小さい木を大きい木に吸収させる
            if self.size( rx ) < self.size( ry ):
                rx, ry = ry, rx
            self.dim[ rx ] += self.dim[ ry ]
            self.edge[ rx ] += self.edge[ ry ] + 1
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
    
    def edge_num( self, x ):
        return self.edge[ self.root( x ) ]

tree = UnionFind( 401000 )

root = [ False for _ in range( 401000 ) ]
for ( a, b ) in ab:
    tree.union( a, b )

for ( a, b ) in ab:
    root[ tree.root( a ) ] = True
    root[ tree.root( b ) ] = True

ans = 0
for r in range( len( root ) ):
    if root[ r ] == True:
        ans += min( tree.size( r ), tree.edge_num( r ) )

print( ans )