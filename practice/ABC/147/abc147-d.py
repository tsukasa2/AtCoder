N = int( input() )
A = list( map( int, input().split() ) )
MOD = 10 ** 9 + 7

one = [ 0 for _ in range( 100 ) ]
# one[ i ] = 下1桁目が1の数の個数

for a in A:
    a_bin = bin( a )[ 2 : ]
    for i, d in enumerate( a_bin[ ::-1 ] ):
        one[ i ] += int( d )

ans = 0
for i, c in enumerate( one ):
    ans += ( c * ( N - c ) % MOD ) * pow( 2, i, MOD ) % MOD
    ans %= MOD

print( ans )