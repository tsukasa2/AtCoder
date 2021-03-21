n = int( input() )
x = list( map( int, input().split() ) )

mean = int( sum( x ) / len( x ) + 0.5 + ( 10 ** -10 ) )

var = 0
for x_i in x:
    var += ( x_i - mean ) ** 2

print( var )