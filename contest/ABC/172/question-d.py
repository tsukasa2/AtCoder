n = int( input() )

# cnt_list = [ 0 for _ in range( n + 1 ) ]

# for i in range( 1, n + 1 ):
#     for c in range( 1, n // i + 1 ):
#         cnt_list[ c * i ] += 1

ans = 0
for i in range( 1, n+1 ):
    ans += ( i + ( n // i ) * i ) * ( n // i ) // 2 

print( ans )