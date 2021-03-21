S = str( input() )

count = [ 0 for _ in range( 10 ) ]

for d in S:
    count[ int( d ) ] += 1

flag = False
for i in range( 125 ):
    n = str( 8 * i ).zfill( 3 )
    d_1, d_2, d_3 = map( int, n )

    count_i = [ 0 for _ in range( 10 ) ]
    count_i[ d_1 ] += 1
    count_i[ d_2 ] += 1
    count_i[ d_3 ] += 1

    if count_i[ d_1 ] <= count[ d_1 ]:
        if count_i[ d_2 ] <= count[ d_2 ]:
            if count_i[ d_3 ] <= count[ d_3 ]:
                flag = True

if len( S ) == 1:
    if int( S ) % 8 == 0:
        flag = True
    else:
        flag = False

if len( S ) == 2:
    if int( S ) % 8 == 0 or int( S[::-1] ) % 8 == 0:
        flag = True
    else:
        flag = False

if flag == True:
    print( "Yes" )
else:
    print( "No" )
