n = int( input() )
v = list( map( int, input().split() ) )

odd = [ 0 for _ in range( 10 ** 5 ) ]
even = [ 0 for _ in range( 10 ** 5 ) ]

for k in range( n ):
    if k % 2 == 0:
        even[ v[ k ] - 1 ] += 1
    else:
        odd[ v[ k ] - 1 ] += 1

odd_1st = ( 0, -1 )
odd_2nd = ( 0, -1 )
even_1st = ( 0, -1 )
even_2nd = ( 0, -1 )

for k in range( 10 ** 5 ):
    if odd[ k ] > odd_1st[ 1 ]:
        odd_2nd = odd_1st
        odd_1st = ( k, odd[ k ] )
    elif odd[ k ] > odd_2nd[ 1 ]:
        odd_2nd = ( k, odd[ k ] )

for k in range( 10 ** 5 ):
    if even[ k ] > even_1st[ 1 ]:
        even_2nd = even_1st
        even_1st = ( k, even[ k ] )
    elif even[ k ] > even_2nd[ 1 ]:
        even_2nd = ( k, even[ k ] )

# print( odd_1st, odd_2nd, even_1st, even_2nd )

if odd_1st[ 0 ] != even_1st[ 0 ]:
    print( n - odd_1st[ 1 ] - even_1st[ 1 ] )
else:
    ans1 = n - odd_2nd[ 1 ] - even_1st[ 1 ]
    ans2 = n - odd_1st[ 1 ] - even_2nd[ 1 ]
    print( min( ans1, ans2 ) )