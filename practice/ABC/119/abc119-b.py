N = int( input() )
xu = [ tuple( map( str, input().split() ) ) for _ in range( N ) ]

JPY_per_BTC = 380000

ans = 0.0
for x, u in xu:
    if u == "JPY":
        ans += float( x )
    else:
        ans += float( x ) * JPY_per_BTC

print( ans )