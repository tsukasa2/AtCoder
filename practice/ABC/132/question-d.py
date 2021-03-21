n, k = map( int, input().split() )
p = 10 ** 9 + 7

inv = [ 0, 1 ]      # iの逆元
fact = [ 1, 1 ]     # iの階乗
factinv = [ 1, 1 ]  # iの階乗の逆元
for i in range( 2, 2001 ):
    fact = fact + [ fact[-1] * i % p ]
    inv = inv + [ - inv[p%i] * (p//i) % p ]
    factinv = factinv + [ factinv[-1] * inv[-1] % p ]

numerator = fact[ k-1 ] * fact[ n-k+1 ] % p
for i in range( 1, k+1 ):
    if n-k-i+1 >= 0:
        ans = numerator * factinv[ k-i ] % p
        ans = ans * factinv[ i-1 ] % p
        ans = ans * factinv[ n-k-i+1 ] % p
        ans = ans * factinv[ i ] % p
        print( ans )
    else:
        print( "0" )