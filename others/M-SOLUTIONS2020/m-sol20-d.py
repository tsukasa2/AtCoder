n = int( input() )
a = list( map( int, input().split() ) )

money = 1000
kabu = 0

a.append( -1 )
c = [ 0 for _ in range( n + 1 ) ]
for i in range( n ):
    if a[ i ] < a[ i + 1 ]:
        c[ i ] = 1
    elif a[ i ] == a[ i + 1 ]:
        c[ i ] = 0
    else:
        c[ i ] = -1

for i in reversed( range( n ) ):
    if c[ i ] == 0:
        c[ i ] = c[ i + 1 ]

for d in range( n ):
    if c[ d ] > 0:
        kabu += money // a[ d ]
        money = money % a[ d ]
    else:
        money += kabu * a[ d ]
        kabu = 0

print( money )