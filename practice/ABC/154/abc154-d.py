n, k = map( int, input().split() )
p = list( map( int, input().split() ) )

sum_k = sum( p[ : k ] )
max_sum_k = sum_k

for i in range( k, n ):
    sum_k += p[ i ] - p[ i - k ]
    if sum_k > max_sum_k:
        max_sum_k = sum_k

print( ( max_sum_k + k ) / 2 )