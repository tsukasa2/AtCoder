n = int( input() )
a = list( map( int, input().split() ) )

step = 0
max_a = a[ 0 ]

for i in range( n ):
    if a[ i ] > max_a:
        max_a = a[ i ]
    else:
        step += ( max_a - a[ i ] )

print( step )