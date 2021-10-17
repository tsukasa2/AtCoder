from itertools import chain, combinations
def powerset( iterable ):
    # powerset( [ 1, 2, 3 ] )
    # --> () ( 1, ) ( 2, ) ( 3, ) ( 1, 2 ) ( 1, 3 ) ( 2, 3 ) ( 1, 2, 3 )
    s = list( iterable )
    return chain.from_iterable( combinations( s, r ) for r in range( len( s ) + 1 ) )

MOD = 10 ** 9 + 7

H, W, K = map( int, input().split() )

DP = [ [ 0 ] * W for _ in range( H + 1 ) ]
DP[ 0 ][ 0 ] = 1
for h in range( H ):
    for p in powerset( range( W - 1 ) ):
        continue_flag = False
        for w in p:
            if w + 1 in p:
                continue_flag = True
        
        if continue_flag:
            continue

        for w in range( W ):
            if w in p:
                DP[ h + 1 ][ w + 1 ] += DP[ h ][ w ]
                DP[ h + 1 ][ w + 1 ] %= MOD
            elif w - 1 in p:
                DP[ h + 1 ][ w - 1 ] += DP[ h ][ w ]
                DP[ h + 1 ][ w - 1 ] %= MOD
            else:
                DP[ h + 1 ][ w ] += DP[ h ][ w ]
                DP[ h + 1 ][ w ] %= MOD

# print( *DP, sep = "\n" )
print( DP[ H ][ K - 1 ] )