# ABC190 F

class Bit:
    # 1-indexed
    def __init__( self, n ):
        self.size = n
        self.tree = [ 0 ] * ( n + 1 )
 
    def sum( self, i ):
        s = 0
        while i > 0:
            s += self.tree[ i ]
            i -= i & -i
        return s
 
    def add( self, i, x ):
        while i <= self.size:
            self.tree[ i ] += x
            i += i & -i

N = int( input() )
a = list( map( int, input().split() ) )

tree = Bit( N )
switch = 0
for a_i in a:
    switch += tree.sum( N ) - tree.sum( a_i )
    # すでに出現した要素のうちa_iより大きいものをカウント
    tree.add( a_i + 1, 1 )

for a_i in a:
    print( switch )
    switch += tree.sum( N ) - tree.sum( a_i + 1 )
    switch -= tree.sum( a_i )