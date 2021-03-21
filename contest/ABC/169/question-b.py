n = int( input() )
a = list( map( int, input().split() ) )

LIMIT = 18

for a_i in a:
    if a_i == 0:
        print( 0 )
        exit()

ans = 1
for a_i in a:
    if len( str( ans ) ) + len( str( a_i ) ) > LIMIT + 2:
        print( -1 )
        break
    elif len( str( ans ) ) + len( str( a_i ) ) > LIMIT:
        if ans * a_i > 10 ** 18:
            print( -1 )
            break
    ans *= a_i
else:
    print( ans )