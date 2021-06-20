N = int( input() )
A = list( map( int, input().split() ) )

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

tree = UnionFind( max( A ) + 1 )
for i in range( N // 2 ):
    if not A[ i ] == A[ - ( i + 1 ) ]:
        tree.union( A[ i ], A[ - ( i + 1 ) ] )

parents = set()
for i in range( max( A ) + 1 ):
    if i == tree.par[ i ]:
        parents.add( i )

ans = 0
for i in parents:
    ans += tree.dim[ i ] - 1

print( ans )