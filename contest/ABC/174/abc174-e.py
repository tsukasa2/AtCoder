import copy

n, k = map( int, input().split() )
a = list( map( int, input().split() ) )

sum_a = sum( a )

devide = [ k * a[ i ] // sum_a for i in range( n ) ]
dev_len = [ a[ i ] / ( devide[ i ] + 1 ) for i in range( n ) ]
k -= sum( devide )
dev_len = list( map( float, dev_len ) )

for _ in range( k ):
    max_i = dev_len.index( max( dev_len ) )
    devide[ max_i ] += 1
    dev_len[ max_i ] = a[ max_i ] / ( devide[ max_i ] + 1 )

print( int( max( dev_len ) + 0.5 ) )