N = 2 * 10 ** 5

MOD = 10 ** 9 + 7

inv = [ 1, 1 ]
fact = [ 1, 1 ]
inv_fact = [ 1, 1 ]
for k in range( 2, N + 1 ):
    inv_k = ( -inv[ MOD % k ] * ( MOD // k ) ) % MOD
    inv.append( inv_k )
    fact.append( fact[ -1 ] * k % MOD )
    inv_fact.append( inv_fact[ -1 ] * inv[ k ] % MOD )

def comb( x, y ):
    return fact[ x ] * inv_fact[ y ] * inv_fact[ x - y ] % MOD

print( comb( 100, 98 ) )