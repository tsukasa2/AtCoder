K = int( input() )
S = str( input() )
T = str( input() )
 
def score( cards ):
    count = [ 0 for _ in range( 9 ) ]
 
    for card in cards:
        count[ int( card ) - 1 ] += 1
 
    res = 0
    for d in range( 9 ):
        res += ( d + 1 ) * ( 10 ** ( count[ d ] ) )
 
    return res
 
deck = [ K for _ in range( 9 ) ]
for c in S[ : -1 ]:
    deck[ int( c ) - 1 ] -= 1
for c in T[ : -1 ]:
    deck[ int( c ) - 1 ] -= 1

ans = 0
for i in range( 1, 10 ):
    for j in range( 1, 10 ):
        if score( S[ : -1 ] + str( i ) ) > score( T[ : -1 ] + str( j ) ):
            if i == j and deck[ i - 1 ] > 1:
                ans += deck[ i - 1 ] * ( deck[ i - 1 ] - 1 )
            else:
                if deck[ i - 1 ] > 0 and deck[ j - 1 ] > 0:
                    ans += deck[ i - 1 ] * deck[ j - 1 ]
 
print( ans / ( ( 9 * K - 8 ) * ( 9 * K - 9 ) ) )