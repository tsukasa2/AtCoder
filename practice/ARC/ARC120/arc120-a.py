N = int( input() )
A = list( map( int, input().split() ) )

sum_k = 0 # sum_k = A_1 + A_2 + ... + A_k
ans_k = 0 # ans_k = f( a ) ( a = ( A_1, A_2, ... , A_k )のとき )
A_max = -1

for k, A_k in enumerate( A ):
    A_max = max( A_max, A_k )
    sum_k += A_k
    ans_k += sum_k
    print( ans_k + ( k + 1 ) * A_max )