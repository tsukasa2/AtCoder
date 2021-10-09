MOD = 998244353

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
            self.tree[ i ] %= MOD
            i += i & -i

N = int( input() )
A = list( map( int, input().split() ) )

bin_inv = [ 1, 1, 499122177 ]
for _ in range( N ):
    inv_k = ( bin_inv[ -1 ] * bin_inv[ 2 ] ) % MOD
    bin_inv.append( inv_k )

A_2 = [ ( a, i ) for i, a in enumerate( A ) ]
A_2.sort()
order_A = [ -1 ] * N # A[ i ]は小さい方からorder_A[ i ]番目
for j, ( _, i ) in enumerate( A_2 ):
    order_A[ i ] = j

tree = Bit( N )
B = [ 0 ] * N # 解説にあるやつ
for i, a in enumerate( A ):
    j = order_A[ i ]
    B[ i ] += tree.sum( j + 1 )
    tree.add( j + 1, bin_inv[ i + 1 ] )

ans = 0
for i in range( 1, N ):
    ans += B[ i ] * pow( 2, i - 1, MOD )
    ans %= MOD

print( ans )