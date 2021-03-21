N = str( input() )
digit = list( map( int, N ) )
N = int( N )

count = [ 0, 0, 0 ]
sum_d = 0
for d in digit:
    count[ d % 3 ] += 1
    sum_d = ( sum_d + d ) % 3

if sum_d == 0:
    print( 0 )
elif sum_d == 1:
    if count[ 1 ] > 0 and N > 9:
        print( 1 )
    elif count[ 2 ] > 1 and N > 99:
        print( 2 )
    else:
        print( -1 )
else:
    if count[ 2 ] > 0 and N > 9:
        print( 1 )
    elif count[ 1 ] > 1 and N > 99:
        print( 2 )
    else:
        print( -1 )
