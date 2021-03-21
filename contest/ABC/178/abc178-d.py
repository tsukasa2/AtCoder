s = int( input() )
mod = 10 ** 9 + 7

fact = [ 1, 1 ]
inv = [ 1, 1 ]
inv_fact = [ 1, 1 ]

for k in range( 2, 2000 ):
    fact.append( fact[ k-1 ] * k % mod )
    inv_k = ( - inv[ mod % k ] * ( mod // k ) % mod ) % mod
    inv.append( inv_k )
    inv_fact.append( inv_fact[ k - 1 ] * inv_k % mod )

# print( inv_fact[:5] )

ans = 0
for k in range( 1, s // 3 + 1 ):
    comp = fact[ s - 2 * k - 1 ] * inv_fact[ s - 3 * k ] % mod
    comp = comp * inv_fact[ k - 1 ] % mod
    ans = ( ans + comp ) % mod

print( ans )