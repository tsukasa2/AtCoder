t = int( input() )
MOD = 1000000007
ans_list = []

for _ in range( t ):
    n, a, b = map( int, input().split() )
    if n < a + b:
        ans = 0
    else:
        ans_b = ( ( n - a - b + 2 ) * ( n - a - b + 1 ) ) #% MOD
        ans_b = ( ans_b // 2 ) % MOD
        
        ans = ( ans_b * 2 ) % MOD
        ans = ( ans * ( n - a + 1 ) ) % MOD
        ans = ( ans * ( n - b + 1 ) ) % MOD
        
        ans = ( ans * 2 ) % MOD

        ans = ( ans - ( ans_b * ans_b ) * 4 ) % MOD
        
        # print( ans_b )
    ans_list.append( str( ans ) )

# print( " ".join( ans_list ) )
for i in range( t ):
    print( ans_list[ i ] )