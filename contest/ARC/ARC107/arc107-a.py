A, B, C = map( int, input().split() )

MOD = 998244353

sum_A = ( A * ( A + 1 ) ) // 2
sum_B = ( B * ( B + 1 ) ) // 2
sum_C = ( C * ( C + 1 ) ) // 2

ans = sum_A % MOD
ans = ans * sum_B % MOD
ans = ans * sum_C % MOD

print( ans )