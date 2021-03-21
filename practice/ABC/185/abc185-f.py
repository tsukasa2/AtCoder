import sys
sys.setrecursionlimit( 10 ** 9 )

class segment_tree:
    def __init__( self, n, e = 0 ):
        # n: 要素数, e: 単位元
        self.element = e
        self.num_leaf = 1 << ( n - 1 ).bit_length() # = n以上で最小の2 ** x
        self.node = [ self.element for _ in range( self.num_leaf * 2 ) ]
    
    def update( self, x, val ):
        # xにvalを代入
        i = self.num_leaf - 1 # 1番目の葉
        i += x
        self.node[ i ] = val
        while True:
            p = ( i - 1 ) // 2 # 親
            self.node[ p ] = self.node[ 2 * p + 1 ] ^ self.node[ 2 * p + 2 ]
            i = p
            if i == 0:
                break
    
    def get_leaf( self, i ):
        return self.node[ self.num_leaf - 1 + i ]
    
    def get( self, left, right, i = 0, left_node = 0, depth = 0 ):
        # 区間[ left, right ]: クエリの範囲
        # i: nodeのindex
        # left_node: node[ i ]が受け持つ区間の左
        # depth: いまの深さ
        width = self.num_leaf // ( 2 ** depth )
        right_node = left_node + width - 1

        if right_node < left or right < left_node:
        # エラー？
            return self.element
    
        elif left <= left_node and right_node <= right:
            return self.node[ i ]
        
        else:
        # 区間[ left_node, right_node ]がクエリからはみ出すとき
            val_l = self.get( left, right, 2 * i + 1, left_node, depth + 1 )
            val_r = self.get( left, right, 2 * i + 2, left_node + width // 2, depth + 1 )
            return val_l ^ val_r

N, Q = map( int, input().split() )
A = list( map( int, input().split() ) )
# query = [ ( map( int, input().split() ) ) for _ in range( Q ) ]

tree = segment_tree( N )

for i, a in enumerate( A ):
    tree.update( i, a )

ans = []
for _ in range( Q ):
    T, X, Y = map( int, input().split() )
    if T == 1:
        tree.update( X - 1, tree.get_leaf( X - 1 ) ^ Y )
    else:
        ans.append( tree.get( X - 1, Y - 1 ) )

for a in ans:
    print( a )