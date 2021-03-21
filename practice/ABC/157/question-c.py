n, m = map( int, input().split() )
s = []
c = []
for _ in range( m ):
    s_i, c_i = map( int, input().split() )
    s.append( s_i )
    c.append( c_i )

if n == 1:
    init = 0
    limit = 10
elif n == 2:
    init = 10
    limit = 100
else:
    init = 100
    limit = 1000

for k in range( init, limit ):
    judge = 1
    for i in range( m ):
        if str( k )[ s[ i ] - 1 ] != str( c[ i ] ):
            judge = 0
    if judge == 1:
        print( k )
        exit()

print( -1 )