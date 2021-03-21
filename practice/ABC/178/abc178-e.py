N = int( input() )
x, y = [], []
for _ in range( N ):
    x_i, y_i = map( int, input().split() )
    x.append( x_i )
    y.append( y_i )

plus = []   # plus[ i ] = x[ i ] + y[ i ]
minus = []  # minus[ i ] = x[ i ] - y[ i ]

for i in range( N ):
    plus.append( x[ i ] + y[ i ] )
    minus.append( x[ i ] - y[ i ] )

ans_1 = max( plus ) - min( plus )
ans_2 = max( minus ) - min( minus )

print( max( ans_1, ans_2 ) )