def calc_score( hand ):
    score = 0
    count = [ 0 for _ in range( 10 ) ]
    # count[ i ] = handに含まれるiの枚数
    for c in hand:
        count[ int( c ) ] += 1
    for k in range( 10 ):
        score += k * 10 ** count[ k ]
    return score

K = int( input() )
S = str( input() )[ : 4 ]
T = str( input() )[ : 4 ]

deck = [ K for _ in range( 10 ) ]
# deck[ i ] = 山札に残っているiの枚数

for c in S:
    deck[ int( c ) ] -= 1
for c in T:
    deck[ int( c ) ] -= 1

kachisuzi = 0
for i in range( 1, 10 ):
    for j in range( 1, 10 ):
        # 裏向きのカード2枚を全探索する
        if i == j:
            if deck[ i ] > 1:
                if calc_score( S + str( i ) ) > calc_score( T + str( j ) ):
                    kachisuzi += deck[ i ] * ( deck[ i ] - 1 )
        else:
            if deck[ i ] > 0 and deck[ j ] > 0:
                if calc_score( S + str( i ) ) > calc_score( T + str( j ) ):
                    kachisuzi += deck[ i ] * deck[ j ]
        print( i, j, kachisuzi )

D = 9 * K - 8
print( kachisuzi / ( D * ( D - 1 ) ) )