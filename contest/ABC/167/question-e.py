# n, m, k = map( int, input().split() )
# p = 998244353

# inv = [ 0, 1 ]
# for i in range( 2, 2 * ( 10 ** 5 ) ):
#     inv.append( - inv[ p % i ] * (p//i) % p )

# paint = [ m ]
# for _ in range( n-1 ):
#     paint[0] = paint[0] * ( m - 1 ) % p

# for i in range( 1, k+1 ):
#     # paint = paint + [ ( paint[-1] * ( n - i ) // i // ( m - 1 ) ) ]
#     x = paint[-1] * ( n - i ) % p
#     x = x * inv[i] % p
#     x = x * inv[ m - 1 ] % p
#     paint.append( x )

# sum_paint = 0
# for i in range( k+1 ):
#     sum_paint = ( sum_paint + paint[i] ) % p

# #print( paint )
# print( sum_paint )

##########以下カンニング###########
n, m, k = map( int, input().split() )
p = 998244353

fact = [ 1, 1 ]       # fact[k] = k!
inv = [ 0, 1 ]        # inv[k] = k^(-1)
fact_inv = [ 1, 1 ]   # fact_inv[k] = (k!)^(-1)
powm_1 = [ 1, m-1 ]
for a in range( 2, 2 * ( 10 ** 5 ) + 1 ):
    fact.append( a * fact[-1] % p )
    inv.append( - inv[p%a] * (p//a) % p )
    fact_inv.append( fact_inv[-1] * inv[a] % p )
    powm_1.append( powm_1[-1] * (m-1) % p )

ans = 0
for i in range( k + 1 ):
    ans = ( ans + m * powm_1[n-1-i] * fact[n-1] * fact_inv[n-1-i] * fact_inv[i] ) % p

print( ans )
