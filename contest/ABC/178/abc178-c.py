n = int( input() )
mod = 10 ** 9 + 7

def njou( x, k ):
    if k == 1:
        return x % mod
    else:
        return njou( x, k - 1 ) * x % mod

# ans = njou( 10, n )
# ans = ans - 2 * ( njou( 9, n ) % mod )
# ans = ( ans + njou( 8, n ) ) % mod
# print( ans )

ans = pow( 10, n, mod )
ans = ans - 2 * pow( 9, n, mod )
ans = ( ans + pow( 8, n, mod ) ) % mod
print( ans )