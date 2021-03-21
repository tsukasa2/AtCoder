n, d = map( int, input().split() )
x = []
y = []
for _ in range( n ):
    x_i, y_i = map( int, input().split() )
    x.append( x_i )
    y.append( y_i )

ans = 0
for i in range( n ):
    if x[ i ] ** 2 + y[ i ] ** 2 <= d ** 2:
        ans += 1

print( ans )