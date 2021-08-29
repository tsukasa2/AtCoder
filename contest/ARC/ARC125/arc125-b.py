N = int( input() )
MOD = 998244353

# x ^ 2 - y = z ^ 2とすると
# y = ( x + z ) * ( x - z )
# p = x + z, q = x - zとすると
# p * q <= N, p >= q, p > 0, q > 0
# よって0 < q <= N ** 0.5
# また，qの値が固定されたとき
# 1 <= y = q * ( q + 2 * z ) <= Nより
# ( 1 // q - q ) // 2 <= z <= ( N // q - q ) // 2
# これとz >= 0より
# 0 <= z <= ( N // q - q ) // 2
ans = 0
for q in range( 1, int( N ** 0.5 ) + 1 ):
    ans += ( N // q - q ) // 2 + 1
    ans %= MOD

print( ans )