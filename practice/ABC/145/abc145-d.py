X, Y = map( int, input().split() )

MOD = 10 ** 9 + 7

inv = [ 1, 1 ]
fact = [ 1, 1 ]
inv_fact = [ 1, 1 ]
for k in range( 2, 10 ** 6 + 1 ):
    inv_k = ( -inv[ MOD % k ] * ( MOD // k ) ) % MOD
    inv.append( inv_k )
    fact.append( fact[ -1 ] * k % MOD )
    inv_fact.append( inv_fact[ -1 ] * inv[ k ] % MOD )

def comb( x, y ):
    return fact[ x ] * inv_fact[ y ] * inv_fact[ x - y ] % MOD

if ( 2 * X - Y ) % 3 != 0 or ( 2 * Y - X ) % 3 != 0:
    print( 0 )
elif ( 2 * X - Y ) < 0 or ( 2 * Y - X ) < 0:
    print( 0 )
else:
    n = ( 2 * X - Y ) // 3
    m = ( 2 * Y - X ) // 3
    print( comb( n + m, n ) )